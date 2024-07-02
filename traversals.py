from abc import ABC, abstractmethod
from typing import Iterable, Optional, Sequence
from graph import Graph
from mytypes import Node
from collections import deque

Path = Sequence[Node]


class Traversal(ABC):
    @abstractmethod
    def search(self, g: Graph, src: Node, dst: Node) -> Optional[Path]: ...


class BFS(Traversal):
    def search(self, g: Graph, src: Node, dst: Node) -> Optional[Path]:
        q: deque[tuple[Node, ...]] = deque()
        q.append((src,))

        while len(q) > 0:
            trail = q.popleft()
            curr_node = trail[0]

            if curr_node == dst:
                return tuple(reversed(trail))

            for v in g.adjacency_map[curr_node]:
                q.append((v,) + trail)

        return None
