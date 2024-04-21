import math
from random import randint
from projekt.models.models import Point

points = []
for _ in range(100):
    x = randint(-100, 100)
    y = randint(-100, 100)
    points.append(Point(x, y))

for point in points:
    print(f'({point.x}, {point.y})', end=" ")