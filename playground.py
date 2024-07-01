from typing import TypeAlias

Node: TypeAlias = str

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
    
# Create an instance of the Graph class
graph = Graph()

# Add nodes to the graph
graph.add_node('A')
graph.add_node('B')
graph.add_node('D')

# Add edges to the graph
graph.add_edge('A', 'B')
graph.add_edge('A', 'D')
graph.add_edge('B', 'D')
graph.add_edge('D', 'A')

print(graph)
    

