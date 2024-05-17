import math
from scipy.spatial import Delaunay
import numpy as np
from .is_connected import is_connected
import matplotlib.pyplot as plt
import io
def calculate_distance(point1, point2):
    return round(math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

def visualize_fence(points, factory, hull_points):
    points = [tuple(point) for point in points]
    hull_points = [tuple(point) for point in hull_points]
    points = [factory] + points
    points_id = {i: tuple(point) for i, point in enumerate(points)}
    
    tri = Delaunay(points)
    indices = tri.simplices
    neighbors = {}

    for triangle in indices:
        for i in range(3):
            start_point_id = triangle[i]
            end_point_id = triangle[(i+1)%3]
            
            if start_point_id not in neighbors:
                neighbors[start_point_id] = []
            
            if end_point_id not in neighbors[start_point_id]:
                neighbors[start_point_id].append(end_point_id)
    neighbors = {key: neighbors[key] for key in sorted(neighbors)}      

    final_neighbors = {}

    for key, values in neighbors.items():
        if points_id[key] not in hull_points: 
            final_neighbors[key] = values.copy()

            for value in values:
                if key in neighbors[value]:
                    neighbors[value].remove(key)



    import networkx as nx
    G = nx.DiGraph()

    for node, edges in final_neighbors.items():
        for edge in edges:
            weight = calculate_distance(points[node], points[edge])
            G.add_edge(node, edge, weight=weight)

    pos = nx.shell_layout(G) 
    weights = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()

    buf.seek(0)
    image_data = buf.getvalue() 
    
    print(final_neighbors)

    return image_data, final_neighbors