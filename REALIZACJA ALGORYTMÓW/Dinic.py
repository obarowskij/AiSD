import heapq

class PathNotFoundException(Exception):
    pass 

class Node:
    def __init__(self,name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name
    
    def __hash__(self):
        return hash(self.name)

class Edge:
    def __init__(self,froom,to,cost,flow):
        self.froom = froom
        self.to = to
        self.cost = cost
        self.flow = flow

    def __str__(self):
        return f'{self.froom.name} {self.to.name} {self.cost} {self.flow}'
    
    def delete_edge(self):
        self.cost = 99999 
    
class Graf:
    def __init__(self):
        self.Nodes = []
        self.Edges = []
        self.max_value = 0


    def add_node(self,Node):
        self.Nodes.append(Node)


    def add_edge(self,Edge):
        self.Edges.append(Edge)
        self.max_value += Edge.flow
    
s = Node("s")
x = Node("x")
u = Node("u")
y = Node("y")
w = Node("w")
t = Node("t")

e1 = Edge(s,x,1,4)
e2 = Edge(x,u,9,5)
e3 = Edge(s,y,9,5)
e4 = Edge(x,y,1,2)
e5 = Edge(y,w,1,2)
e6 = Edge(w,t,9,3)
e7 = Edge(w,u,1,3)
e8 = Edge(u,t,1,5)


G = Graf()


G.add_node(s)
G.add_node(x)
G.add_node(u)
G.add_node(y)
G.add_node(w)
G.add_node(t)


G.add_edge(e1)
G.add_edge(e2)
G.add_edge(e3)
G.add_edge(e4)
G.add_edge(e5)
G.add_edge(e6)
G.add_edge(e7)
G.add_edge(e8)


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph.Nodes}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()
    previous_nodes = {}
    previous_edges = {}
    min_flow = float('inf')  # Initialize min_flow to infinity

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        if current_node in visited:
            continue

        visited.add(current_node)

        for edge in graph.Edges:
            if edge.froom == current_node:
                neighbor = edge.to
                distance = current_distance + edge.cost

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    previous_edges[neighbor] = edge
                    heapq.heappush(queue, (distance, neighbor))

    if end not in previous_nodes:
        raise PathNotFoundException("No path found")
    
    path_nodes = []
    path_edges = []
    current = end
    while current is not None:
        path_nodes.append(current)
        if current != start:
            path_edges.append(previous_edges[current])
            # Update min_flow with the minimum flow found so far
            min_flow = min(min_flow, previous_edges[current].flow)
        current = previous_nodes.get(current)
    path_nodes.reverse()
    path_edges.reverse()
    return distances[end], path_nodes, path_edges, min_flow
path_available = True
start_node = s
end_node = t
max_flow = 0
cost = 0
while path_available:
    try:
        lowest_cost, path_nodes, path_edges, min_flow = dijkstra(G, start_node, end_node)
        if min_flow == 0:
            raise PathNotFoundException("No path found")
        print(f"Najniższy koszt od {start_node.name} do {end_node.name}: {lowest_cost}")
        print("Droga (wierzchołki):", ' -> '.join(node.name for node in path_nodes))
        print("Droga (krawędzie):", ' -> '.join(str(edge) for edge in path_edges))
        for edge in path_edges:
            cost += edge.cost * min_flow
            edge.flow -= min_flow
            if edge.flow == 0:
                edge.delete_edge()
        print(f"Minimalny przepływ: {min_flow}")
        max_flow += min_flow
    except PathNotFoundException:
        path_available = False
        print(f"Maksymalny przeplyw: {max_flow}")
        print(f"Koszt: {cost}")
