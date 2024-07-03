import z3
from typing import TypeVar, Optional, Iterable
from dataclasses import dataclass
from automaton import Automaton
from graph import Graph, NodeAttributes
from mytypes import Node
from collections import deque


K = TypeVar("K")
V = TypeVar("V")


@dataclass(frozen=True)
class RunContext:
    run: list[str]
    accumulated_formulas: list[any]
    # any here is actually a z3 formula, with variables already subst-ed in

    def extend_with(self, state: str, formula: any) -> "RunContext":
        updated_run: list[str] = self.run.copy()
        updated_formula: list[any] = self.accumulated_formulas.copy()

        updated_run.append(state)
        updated_formula.append(formula)

        return RunContext(
            run=updated_run,
            accumulated_formulas=updated_formula,
        )

    @property
    def current_state(self):
        return self.run[-1]

    @property
    def path_index(self):
        return len(self.run)


class DataUtils:
    @staticmethod
    def merge_dicts(dict1: dict[K, V], dict2: dict[K, V]) -> dict[K, V]:
        common_keys = set(dict1.keys()) & set(dict2.keys())
        if common_keys:
            raise ValueError(
                f"Key(s) {common_keys} are present in both dictionaries and would be overwritten"
            )

        return {**dict1, **dict2}

    # def __query_with_naive_algorithm(
    #     attributes: NodeAttributes,
    #     automaton: Automaton,
    #     graph: Graph,
    #     all_variables,
    #     source: Node,
    #     target: Node,
    # ) -> tuple[True, tuple[Node, ...]] | False:
    #     graph_paths = graph.get_paths(source, target)

    #     automaton_graph = automaton.to_graph()
    #     for f in automaton.final_states:
    #         for path in automaton_graph.get_paths(automaton.initial_state, f):
    #             path_formula = z3.And(
    #                 *[
    #                     z3.substitute(
    #                         z3.parse_smt2_string(
    #                             automaton_graph.edge_attributes[(from_state, to_state)],
    #                             decls=all_variables,
    #                         ),
    #                         *zip(
    #                             attributes.alphabet.values(),  # (age, name, hobby)
    #                             attributes.attribute_map[
    #                                 to_vertex
    #                             ],  # (25, 'Alice', None)
    #                         ),
    #                     )
    #                     for from_state, to_state in zip(path, path[1:])
    #                 ]
    #             )

    #             if z3.solve(path_formula) == z3.sat:
    #                 return True, path
    #     return False

    # TODO To be implemented for the second task

    def query_with_naive_algorithm(
        attributes: NodeAttributes,
        automaton: Automaton,
        graph: Graph,
        global_vars,
        source: Node,
        target: Node,
    ) -> Optional[tuple[RunContext, z3.ModelRef]]:

        all_variables = DataUtils.merge_dicts(attributes.alphabet, global_vars)

        def materialize_formula(formula: str, node: Node):
            mapping = (
                (
                    attr,
                    (
                        z3.RealVal(value)
                        if isinstance(value, (int, float))
                        else z3.StringVal(value)
                    ),
                )
                for attr, value in zip(
                    attributes.alphabet.values(),
                    attributes.attribute_map[
                        str(node) if isinstance(node, int) else node
                    ],
                )
            )

            return z3.substitute(
                z3.parse_smt2_string(formula, decls=all_variables)[0],
                *mapping,
            )

        def check_path(
            path: Iterable[Node],
        ) -> Optional[tuple[RunContext, z3.ModelRef]]:
            # does there exist a sequence of transistions in the automaton from q_0 to q_k in F
            # such that the phis accumulated
            assert len(path) >= 2

            solver = z3.Solver()
            worklist = deque[RunContext]()
            worklist.append(
                RunContext(run=[automaton.initial_state], accumulated_formulas=[])
            )

            while len(worklist) > 0:
                ctx = worklist.popleft()
                solver.reset()
                solver.append(z3.And(*ctx.accumulated_formulas))
                result = solver.check()
                if (
                    # not sure about this, check to make sure not off by one
                    ctx.path_index == len(path)
                    and ctx.current_state in automaton.final_states
                    and result == z3.sat
                ):
                    return ctx, solver.model()

                # Compute successors of ctx and add to worklist
                if result != z3.unsat:
                    worklist.extend(
                        ctx.extend_with(
                            state=trans.to_state,
                            formula=materialize_formula(
                                trans.formula,
                                path[ctx.path_index],
                            ),
                        )
                        for trans in automaton.transitions
                        if trans.from_state == ctx.current_state
                        and ctx.path_index < len(path)
                    )

            return None

        # assert all(isinstance(node, str) for node in graph.adjacency_map)
        print(graph.adjacency_map)
        for path in graph.get_paths(source, target):
            result = check_path(path)
            if result is not None:
                return result

        return False

    def query_with_macro_state(
        attribute: NodeAttributes, aut: Automaton, graph: Graph, vars, source, target
    ) -> bool:
        pass

    # TODO To be implemented for the third task
