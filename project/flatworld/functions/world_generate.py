from random import randint
from .models import Point

def generate(input_points):
    points = []
    for _ in range(input_points):
        x = randint(-200, 200)
        y = randint(-200, 200)
        points.append(Point(x, y))
    print(points)
    return points