from collections import defaultdict
 
class Graph:
 
    def __init__(self, graph):
        self.graph = graph 
        self. ROW = len(graph)
        # self.COL = len(gr[0])
 
    def BFS(self, s, t, parent):
 
        visited = [False]*(self.ROW)
 
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            u = queue.pop(0)
 
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        return False
             
     
    def FordFulkerson(self, source, sink):
 
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        while self.BFS(source, sink, parent) :
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            max_flow +=  path_flow

            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
 
   
graph = [[0, 20, 0, 0, 50, 0, 0],
        [0, 0, 50, 0, 0, 60, 0],
        [0, 0, 0, 80, 0, 0, 40],
        [0, 0, 0, 0, 0, 0, 40],
        [0, 10, 0, 0, 0, 30, 0],
        [0, 0, 10, 0, 0, 0, 20],
        [0, 0, 0, 0, 0, 0, 0]]
 
g = Graph(graph)
 
source = 0; sink = 6
  
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
 
