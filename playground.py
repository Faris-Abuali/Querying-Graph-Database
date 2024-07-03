from graph import BFS, DFS, Graph
from json_parser import JSONParser

graph = Graph()

graph.add_edge("1", "2")
graph.add_edge("2", "3")
graph.add_edge("3", "1")

bfs = BFS()
print(list(bfs.search(graph, src="1", dst="3")))

# dfs = DFS()
# print(dfs.search(graph, src="1", dst="3"))


# ------------------ Example 1 ----------------------------
# graph.add_edge("1", "2")
# graph.add_edge("1", "3")
# graph.add_edge("2", "3")
# graph.add_edge("2", "5")
# graph.add_edge("3", "4")
# graph.add_edge("5", "4")

# bfs = BFS()
# print(list(bfs.search(graph, src="1", dst="4")))

# dfs = DFS()
# print(dfs.search(graph, src="1", dst="4"))

# ------------------ Example 2 ----------------------------
# graph.add_edge("1", "2")
# graph.add_edge("1", "3")
# graph.add_edge("1", "4")
# graph.add_edge("1", "5")

# graph.add_edge("2", "3")
# graph.add_edge("2", "4")
# graph.add_edge("2", "5")

# graph.add_edge("3", "4")
# graph.add_edge("3", "5")

# graph.add_edge("4", "5")

# bfs = BFS()
# # print(sorted(bfs.search(graph, src="1", dst="5")))
# print(list(bfs.search(graph, src="1", dst="5")))

# dfs = DFS()
# # print(sorted(dfs.search(graph, src="1", dst="5")))
# print(list(dfs.search(graph, src="1", dst="5")))

# parser = JSONParser("example1.json")
# parser.parse()
# print(parser.automaton)
# print(parser.automaton.to_graph())