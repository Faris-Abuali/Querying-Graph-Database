from graph import Graph
from traversals import BFS, DFS


graph = Graph()

graph.add_edge("1", "2")
graph.add_edge("1", "3")
graph.add_edge("2", "3")
graph.add_edge("2", "5")
graph.add_edge("3", "4")
graph.add_edge("5", "4")

bfs = BFS()
print(bfs.search(graph, src="1", dst="4"))

dfs = DFS()
print(dfs.search(graph, src="1", dst="4"))
