import math


class WeightedGraph:

    def __init__(self):
        self.adjacency_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_dict:
            self.adjacency_dict[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_dict[vertex1].update({vertex2: weight})
        self.adjacency_dict[vertex2].update({vertex1: weight})

    def choose_next_vertex(self, vertex_list, adj_list, vertex, distances):
        index = vertex_list.index(vertex)
        vertex_list.pop(index)
        unvisited_dict = adj_list[vertex].copy()
        for item in list(unvisited_dict):
            if item not in vertex_list:
                unvisited_dict.pop(item)
        if len(unvisited_dict) > 0:
            start = min(unvisited_dict, key=unvisited_dict.get)
            return start

    def dijkstra(self, start):
        # initialized distances, for start 0 and infinite for anything else
        distances = {}
        for vertex in self.adjacency_dict:
            distances.update({vertex: math.inf})
        distances[start] = 0
        # printing unvisited list
        unvisited_list = [vertex for vertex in self.adjacency_dict]
        while len(unvisited_list) > 0:
            # adding neighbours
            if start is None:
                return print(distances)
            neighbours = self.adjacency_dict[start]
            for vertex in neighbours:
                if distances.get(start) + neighbours.get(vertex) < distances.get(vertex):
                    distances[vertex] = distances.get(start) + neighbours.get(vertex)
            start = self.choose_next_vertex(unvisited_list, self.adjacency_dict, start, distances)
        answer = sum(distances.values()) / len(distances)
        return print("The avg sum is: ", answer, "distances: ", distances)


graph = WeightedGraph()

# with open("dijkstra.in", "r") as f:
#     for line in f:
#         line = line.split(' ')
#         graph.add_vertex(int(line[0]))
#         graph.add_vertex(int(line[1]))
#         graph.add_edge(int(line[0]), int(line[1]), int(line[2]))


graph.add_vertex("A")
graph.add_vertex("D")
graph.add_vertex("C")
graph.add_vertex("F")
graph.add_vertex("Y")
graph.add_vertex("Z")
graph.add_vertex("X")

graph.add_edge("A", "C", 2)
graph.add_edge("A", "F", 3)
graph.add_edge("A", "D", 1)
graph.add_edge("C", "D", 4)
graph.add_edge("C", "F", 3)
graph.add_edge("C", "Y", 11)
graph.add_edge("C", "Z", 1)
graph.add_edge("C", "X", 3)
graph.add_edge("D", "X", 7)
graph.add_edge("F", "Y", 8)
graph.add_edge("Z", "Y", 10)
graph.add_edge("Z", "X", 5)

# graph.dijkstra(5)
graph.dijkstra("Y")
