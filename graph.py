from typing import Iterable, Optional, Union
import z3
from mytypes import Node, Z3VarType


class Graph:
    def __init__(self):
        self.nodes: set[Node] = set()
        self.adjacency_map: dict[Node, list[Node]] = {}

    def add_node(self, node: Node):
        self.nodes.add(node)
        if node not in self.adjacency_map:
            self.adjacency_map[node] = []

    def add_edge(self, from_node: Node, to_node: Node):
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_map[from_node].append(to_node)

    def __str__(self):
        result = "Graph:\n"
        for node in sorted(self.nodes):
            result += (
                f"{node}: {', '.join(map(str, self.adjacency_map.get(node, [])))}\n"
            )
        return result


class NodeAttributes:
    def __init__(self):
        self.alphabet: dict[str, Z3VarType] = {}
        self.attribute_map: dict[str, Iterable[str | float]] = {}

    def add_variable(self, var_name: str, value: int | float | str):
        if isinstance(value, (int, float)):
            self.alphabet[var_name] = z3.Real(var_name)  # type: ignore
        elif isinstance(value, str):  # type: ignore
            self.alphabet[var_name] = z3.String(var_name)  # type: ignore
        else:
            raise ValueError("Unsupported attribute type")

    def get_variable(self, var_name: str) -> Optional[Z3VarType]:
        return self.alphabet.get(var_name, None)

    def __str__(self):
        output = "Node Attributes:\n"
        for var_name, value in self.attribute_map.items():
            output += f"{var_name}: {value}\n"
        return output
