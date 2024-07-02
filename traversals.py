from abc import ABC, abstractmethod
from typing import Optional, Sequence
from graph import Graph
from mytypes import Node
from collections import deque

Path = Sequence[Node]


class Traversal(ABC):
    @abstractmethod
    def search(self, g: Graph, src: Node, dst: Node) -> Optional[Path]: ...

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
                return tuple(reversed(trail))

            # If the current node has not been visited yet
            if curr_node not in visited:
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
                return tuple(reversed(trail))

            for v in g.adjacency_map[curr_node]:
                # Append the new path to the queue
                q.append((v,) + trail)
        
        # Return None if no path is found
        return None
