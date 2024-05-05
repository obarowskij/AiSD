from random import randint
from .models import Point


def generate(input_points):
    points = []
    for _ in range(input_points):  # use the input to generate points
        x = randint(-100, 100)
        y = randint(-100, 100)
        points.append(Point(x, y))
    return points
