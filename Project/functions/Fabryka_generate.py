from projekt.models.models import Point
from random import randint
from projekt.functions.Graham_problem1 import hull_points
import math

def det_cubic(p1, p2, p3):
    return p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)

def point_in_polygon(point, polygon):
    num_vertices = len(polygon)
    x, y = point.x, point.y
    inside = False
    p1 = polygon[0]
 
    for i in range(1, num_vertices + 1):
        p2 = polygon[i % num_vertices]
 
        if y > min(p1.y, p2.y):
            if y <= max(p1.y, p2.y):
                if x <= max(p1.x, p2.x):
                    x_intersection = (y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x
 
                    if p1.x == p2.x or x <= x_intersection:
                        inside = not inside
 
        p1 = p2
    return inside

def is_polygon_convex(points):
    n = len(points)
    if n == 3:  # A triangle is always convex
        return True
    else:
        signs = []
        for i in range(n):
            dx1 = points[(i+1)%n].x - points[i].x
            dy1 = points[(i+1)%n].y - points[i].y
            dx2 = points[(i+2)%n].x - points[(i+1)%n].x
            dy2 = points[(i+2)%n].y - points[(i+1)%n].y

            z_cross_product = dx1 * dy2 - dy1 * dx2

            if z_cross_product != 0:
                signs.append(z_cross_product > 0)

        return all(signs) or not any(signs)

if is_polygon_convex(hull_points):
    print("The polygon is convex.")
else:
    print("The polygon is not convex.")
    
is_in_polygon = False
while not is_in_polygon:
    x = randint(-20, 20)
    y = randint(-20, 20)
    factory = Point(x, y)
    is_in_polygon = point_in_polygon(factory, hull_points)
    
print(f'factory: {factory}')