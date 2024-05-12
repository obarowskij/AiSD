import math
from scipy.spatial import Delaunay
import numpy as np
from .is_connected import is_connected
import matplotlib.pyplot as plt
import io

def visualize_fence(points, factory, hull_points):
    points = [tuple(point) for point in points]
    hull_points = [tuple(point) for point in hull_points]
    points = [factory] + points
    points_id = {i: tuple(point) for i, point in enumerate(points)}
    
    tri = Delaunay(points)

    # Get the indices of the points forming the vertices of the triangles
    indices = tri.simplices
    neighbors = {}

    # Iterate over the indices
    for triangle in indices:
        # Each triangle has 3 vertices, so we have 3 edges
        for i in range(3):
            # Get the start and end points of each edge
            start_point_id = triangle[i]
            end_point_id = triangle[(i+1)%3]
            
            # If the start point ID is not already a key in the dictionary, add it with an empty list as its value
            if start_point_id not in neighbors:
                neighbors[start_point_id] = []
            
            # If the end point ID is not already in the list of neighbors for the start point ID, add it
            if end_point_id not in neighbors[start_point_id]:
                neighbors[start_point_id].append(end_point_id)
    neighbors = {key: neighbors[key] for key in sorted(neighbors)}      

    final_neighbors = {}

    for key, values in neighbors.items():
        # Add all neighbors to the key
        if points_id[key] not in hull_points: 
            final_neighbors[key] = values.copy()

            # Remove the key from the values of all its neighbors
            for value in values:
                if key in neighbors[value]:
                    neighbors[value].remove(key)

    # New code to create a set of plotted points
    plotted_points = set()

    # Existing code
    for point_id, neighbor_ids in final_neighbors.items():
        point = points_id[point_id]
        for neighbor_id in neighbor_ids:
            neighbor = points_id[neighbor_id]
            plt.plot([point[0], neighbor[0]], [point[1], neighbor[1]], 'c-')

    # New code to plot and enumerate points
    # New code to plot and enumerate points
    for i, point_id in enumerate(points_id):
        point = points[point_id]
        color = "red" if i == 0 else "green" if point in hull_points else "blue"
        plt.plot(point[0], point[1], 'o', color=color)
        plt.text(point[0], point[1], str(i), color=color, fontsize=12)
        plotted_points.add(tuple(point))

    buf = io.BytesIO()
    plt.savefig(buf, format="png")

    image_data = buf

    return image_data, final_neighbors