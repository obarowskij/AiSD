# def det_cubic(p1, p2, p3):
#         return p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)
# po co to nie pamietam


def is_polygon_convex(points):
    n = len(points)
    if n == 3:  # A triangle is always convex
        return True
    else:
        signs = []
        for i in range(n):
            dx1 = points[(i + 1) % n].x - points[i].x
            dy1 = points[(i + 1) % n].y - points[i].y
            dx2 = points[(i + 2) % n].x - points[(i + 1) % n].x
            dy2 = points[(i + 2) % n].y - points[(i + 1) % n].y

            z_cross_product = dx1 * dy2 - dy1 * dx2

            if z_cross_product != 0:
                signs.append(z_cross_product > 0)

        return all(signs) or not any(signs)
