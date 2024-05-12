from collections import defaultdict, deque

def is_connected(neighbors_of_all_points):
    graph = {id: neighbors for id, neighbors in neighbors_of_all_points.items()}
    if not graph:
        return False
    
    start_vertex = next(iter(graph))  # Start from any vertex
    
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    
    while queue:
        current_vertex = queue.popleft()
        if current_vertex in graph:
            for neighbor in graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    return len(visited) == len(graph)