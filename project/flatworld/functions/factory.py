from .models import Point
from random import randint


def generate_factory(hull_points):
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
                        x_intersection = (y - p1.y) * (p2.x - p1.x) / (
                            p2.y - p1.y
                        ) + p1.x

                        if p1.x == p2.x or x <= x_intersection:
                            inside = not inside

            p1 = p2
        return inside

    hull_points = [Point(*point) for point in hull_points]
    is_in_polygon = False
    while not is_in_polygon:
        x = randint(-200, 200)
        y = randint(-200, 200)
        factory = Point(x, y)
        is_in_polygon = point_in_polygon(factory, hull_points)
    return factory
