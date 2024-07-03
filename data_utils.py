import z3
from typing import TypeVar

from automaton import Automaton
from graph import Graph, NodeAttributes
from mytypes import Node


K = TypeVar("K")
V = TypeVar("V")


class DataUtils:
    @staticmethod
    def merge_dicts(dict1: dict[K, V], dict2: dict[K, V]) -> dict[K, V]:
        common_keys = set(dict1.keys()) & set(dict2.keys())
        if common_keys:
            raise ValueError(
                f"Key(s) {common_keys} are present in both dictionaries and would be overwritten"
            )

        return {**dict1, **dict2}

    def query_with_naive_algorithm(
        attributes: NodeAttributes,
        automaton: Automaton,
        graph: Graph,
        all_variables,
        source: Node,
        target: Node,
    ) -> bool:
        for path in graph.get_paths(source, target):
            path_formula = True
            current_states = {automaton.initial_state}
            current_constraints: list[tuple[list, int]] = []

            for _, to_vertex in zip(path, path[1:]):
                next_states = set()  # TODO: should this be in the following loop?
                next_constraints = []

                for state in current_states:

                    for trans in filter(
                        lambda t: t.from_state == state, 
                        automaton.transitions
                    ):
                        transistion_formula = z3.substitute(
                            z3.parse_smt2_string(trans.formula, decls=all_variables),
                            *zip(
                                attributes.alphabet.items(),
                                attributes.attribute_map[to_vertex],
                            ),
                        )
                        path_acc_formula = z3.And(path_acc_formula, transistion_formula)

                        next_states.add(trans.to_state)
                        next_constraints.append(([
                            *current_constraints,
                            transistion_formula
                        ], trans.to_state))


                

            if z3.solve(path_formula) == z3.sat:
                return True

        return False

    # TODO To be implemented for the second task

    def query_with_macro_state(
        attribute: NodeAttributes, aut: Automaton, graph: Graph, vars, source, target
    ) -> bool:
        pass

    # TODO To be implemented for the third task
