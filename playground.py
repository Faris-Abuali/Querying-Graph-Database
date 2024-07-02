from graph import Graph
from traversals import BFS


graph = Graph()

graph.add_edge("1", "2")
graph.add_edge("1", "3")
graph.add_edge("2", "3")
graph.add_edge("2", "5")
graph.add_edge("3", "4")
graph.add_edge("5", "4")

traversal = BFS()
print(traversal.search(graph, src="1", dst="4"))

