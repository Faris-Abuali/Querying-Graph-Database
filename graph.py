from typing import Iterable, Optional, Union
import z3
from mytypes import Node, Z3VarType
from abc import ABC, abstractmethod
from typing import Optional, Sequence
from mytypes import Node
from collections import deque

Path = Sequence[Node]


class Traversal(ABC):
    @abstractmethod
    def search(self, g: "Graph", src: Node, dst: Node) -> Optional[Path]: ...


class Graph:
    def __init__(self):
        self.nodes: set[Node] = set()
        self.adjacency_map: dict[Node, list[Node]] = {}
        self.edge_attributes: dict[tuple[Node, Node], str] = {}

    def add_node(self, node: Node):
        self.nodes.add(node)
        if node not in self.adjacency_map:
            self.adjacency_map[node] = []

    def add_edge(self, from_node: Node, to_node: Node, meta: str = ""):
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_map[from_node].append(to_node)
        self.edge_attributes[(from_node, to_node)] = meta

    def get_paths(
        self, src: Node, dst: Node, strategy: Optional[Traversal] = None
    ) -> Iterable[Node]:
        traversal = BFS() if strategy is None else strategy
        return traversal.search(self, src, dst)

    def __str__(self):
        result = "Graph:\n"
        for node in sorted(self.nodes):
            result += (
                f"{node}: {', '.join(map(str, self.adjacency_map.get(node, [])))}\n"
            )
            
        meta_info = "\nEdge Attributes:\n"
        for edge in self.edge_attributes:
            meta_info += f"({edge[0]} -> {edge[1]}): {self.edge_attributes[edge]}\n"
        
        return result + meta_info

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


# Depth-First Search (DFS) implementation
class DFS(Traversal):
    def search(self, g: Graph, src: Node, dst: Node) -> Optional[Path]:
        """finds the shortest path from src to dst in graph g.

        Returns:
            Optional[Path]: The path from src to dst if one exists, otherwise None.
        """
        # Stack to hold the paths
        stack: deque[tuple[Node, ...]] = deque()
        stack.append((src,))

        # Set to track visited nodes to avoid cycles
        visited: set[Node] = set()

        # Perform the DFS
        while len(stack) > 0:
            # Get the last path from the stack
            trail = stack.pop()

            # The current node is the last node in the path
            curr_node = trail[0]

            # If the current node is the destination, return the reversed path
            if curr_node == dst:
                yield tuple(reversed(trail))

            # Mark the current node as visited
            visited.add(curr_node)

            # Iterate through the neighbors of the current node
            for v in g.adjacency_map[curr_node]:
                # Append the new path to the stack
                stack.append((v,) + trail)

        # Return None if no path is found
        return None


# Breadth-First Search (BFS) implementation
class BFS(Traversal):
    def search(self, g: Graph, src: Node, dst: Node) -> Optional[Path]:
        """finds the shortest path from src to dst in graph g.

        Returns:
            Optional[Path]: The path from src to dst if one exists, otherwise None.
        """
        q: deque[tuple[Node, ...]] = deque()
        q.append((src,))

        while len(q) > 0:
            # Get the first path from the queue
            trail = q.popleft()
            curr_node = trail[0]

            # The current node is the last node in the path
            if curr_node == dst:
                yield tuple(reversed(trail))

            for v in g.adjacency_map[curr_node]:
                # Append the new path to the queue
                q.append((v,) + trail)

        # Return None if no path is found
        return None
