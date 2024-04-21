from random import randint
import math
from collections import deque
import matplotlib.pyplot as plt
from projekt.models.models import Point, Stack
from projekt.functions.World_generate import points

def det(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    return 1 if val > 0 else 2  # Clockwise or counterclockwise

def calculate_alfa(point, pivot):
    x, y = point.x - pivot.x, point.y - pivot.y
    d = abs(x) + abs(y)
    if d == 0:
        return 0
    if x >= 0 and y >= 0:
        return y / d
    elif x < 0 and y >= 0:
        return 2 - y / d
    elif x <= 0 and y < 0:
        return 2 + abs(y) / d
    elif x>=0 and y<0:
        return 4 - abs(y) / d
    else:
        return -1

min_y = float('inf')
min_index = -1
for i, point in enumerate(points):
    if point.y < min_y or (point.y == min_y and point.x < points[min_index].x):
        min_y = point.y
        min_index = i

points[0], points[min_index] = points[min_index], points[0]
pivot = points[0]
sorted_polar_points = sorted(points[1:], key=lambda p: calculate_alfa(p, pivot))

Graham_stack = Stack()
Graham_stack.push(points[0])
Graham_stack.push(sorted_polar_points[0])
Graham_stack.push(sorted_polar_points[1])
for i in range(1, len(sorted_polar_points)):
    while len(Graham_stack.items) > 1 and det(Graham_stack.items[-2], Graham_stack.items[-1], sorted_polar_points[i]) != 2:
        Graham_stack.pop()
    Graham_stack.push(sorted_polar_points[i])

# Visualization
plt.figure()

# Plot all points
for point in points:
    plt.plot(point.x, point.y, 'bo')

# Transfer points from the Graham_stack to hull_points
hull_points = []
while not Graham_stack.is_empty():
    point = Graham_stack.pop()
    hull_points.append(point)

# Add the first point again to close the hull
hull_points.append(hull_points[0])

# Plot the hull points
for i in range(len(hull_points) - 1):
    plt.plot([hull_points[i].x, hull_points[i+1].x], [hull_points[i].y, hull_points[i+1].y], 'r-')

# Show the plot
plt.show()