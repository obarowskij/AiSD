import networkx as nx
from io import BytesIO
import os


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def visualize_fence(hull, world_points, factory):
    G = nx.DiGraph()

    pass

    # Wczytaj dane obrazu do obiektu BytesIO
    with open("fence.png", "rb") as f:
        image_data = BytesIO(f.read())

    # Ustaw "wskaźnik pliku" na początek obiektu BytesIO
    image_data.seek(0)

    # Usuń plik
    os.remove("fence.png")

    return image_data
