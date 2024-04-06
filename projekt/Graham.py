from random import randint
import math
from collections import deque
import matplotlib.pyplot as plt
from typing import List, Tuple

## PIP INSTALL MATPLOTLIB

class Stack:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'

def det(p1, p2, p3):
    return (p2.y - p1.y) * (p3.x - p2.x) < (p2.x - p1.x) * (p3.y - p2.y)
    
def calculate_alfa(point: Tuple[int, int]) -> float:
    x, y = point.x, point.y
    d = abs(x) + abs(y)
    if d == 0:
        return 0
    if x >= 0 and y >= 0:
        return y / d
    elif x < 0 and y >= 0:
        return 2 - y / d
    elif x <= 0 and y < 0:
        return 2 + abs(y) / d
    else:  # x >= 0 and y < 0
        return 4 - abs(y) / d

def sort_points(points: List[Point]) -> List[Tuple[Point, float]]:
    alfa_points = [(point, calculate_alfa(point)) for point in points]
    alfa_points.sort(key=lambda p: p[1])

    i = 0
    while i < len(alfa_points) - 1:
        if alfa_points[i][1] == alfa_points[i + 1][1]:
            j = i
            while j < len(alfa_points) - 1 and alfa_points[j][1] == alfa_points[j + 1][1]:
                j += 1
            alfa_points[i:j+1] = sorted(alfa_points[i:j+1], key=lambda p: p[0].x)
            i = j
        else:
            i += 1

    return alfa_points



points = []
for _ in range(10):
    x = randint(-10, 10)
    y = randint(-10, 10)
    points.append(Point(x, y))

for point in points:
    print(f'({point.x}, {point.y})', end=" ")

obwodka = []

min_y = points[0].y
min_x = points[0].x
min_point = points[0]
for point in points:
    if point.y < min_y or (point.y == min_y and point.x < min_x):
        min_y = point.y
        min_x = point.x
        min_point = point
print(f'\nNajniższy punkt: ({min_x}, {min_y})')


sorted_polar_points = sort_points(points)
sorted_polar_points = [(min_point, 0)] + sorted_polar_points
for p in sorted_polar_points:
    print(f'({p[0].x}, {p[0].y}, {p[1]:.2f})')
    
Graham_stack = Stack()

for i in range(1,3):
    Graham_stack.push(sorted_polar_points[i][0])

for i in range(3, len(sorted_polar_points)):
    while (len(Graham_stack.items) > 1) and det(Graham_stack.items[-1], Graham_stack.items[-2], sorted_polar_points[i][0]):
        Graham_stack.pop()
    Graham_stack.push(sorted_polar_points[i][0])
print("\nObwódka:")
hull_points = []
temp_stack = Stack()
while not Graham_stack.is_empty():
    point = Graham_stack.pop()
    temp_stack.push(point) 
    print(f'({point.x}, {point.y})', end=" ")
  
#wizualizacja
plt.figure()

# Plot all points
for point in points:
    plt.plot(point.x, point.y, 'bo')

# Transfer points from the temporary stack to hull_points
while not temp_stack.is_empty():
    point = temp_stack.pop()
    hull_points.append(point)

# Add the first point again to close the hull
hull_points.append(hull_points[0])

# Plot the hull points
for i in range(len(hull_points) - 1):
    plt.plot([hull_points[i].x, hull_points[i+1].x], [hull_points[i].y, hull_points[i+1].y], 'r-')

# Show the plot
plt.show()
