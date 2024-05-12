import unittest
import math
from ..functions.is_polygon_convex import is_polygon_convex
from ..models import Point


class TestPolygonConvexity(unittest.TestCase):
    def test_triangle(self):
        # A triangle is always convex
        points = [Point(0, 0), Point(1, 0), Point(0, 1)]
        self.assertTrue(is_polygon_convex(points), "Failed on triangle")

    def test_pentagon(self):
        # A regular pentagon is convex
        points = [
            Point(math.cos(2 * math.pi * i / 5), math.sin(2 * math.pi * i / 5))
            for i in range(5)
        ]
        self.assertTrue(is_polygon_convex(points), "Failed on pentagon")

    def test_L_shape(self):
        # An "L" shape is not convex
        points = [
            Point(0, 0),
            Point(1, 0),
            Point(1, 1),
            Point(0, 1),
            Point(0, 2),
        ]
        self.assertFalse(is_polygon_convex(points), "Failed on 'L' shape")

    def test_star_shape(self):
        # A star shape is not convex
        points = [
            Point(0, 0),
            Point(2, 0),
            Point(3, 2),
            Point(2, 4),
            Point(0, 4),
            Point(1, 2),
        ]
        self.assertFalse(is_polygon_convex(points), "Failed on star shape")

    def test_convex_polygon(self):
        # A regular 20-gon is convex
        convex_points = [
            Point(
                math.cos(2 * math.pi * i / 20), math.sin(2 * math.pi * i / 20)
            )
            for i in range(20)
        ]
        self.assertTrue(
            is_polygon_convex(convex_points), "Failed on convex polygon"
        )

    def test_concave_polygon(self):
        # A regular 20-gon with a concave part is not convex
        concave_points = (
            [
                Point(
                    math.cos(2 * math.pi * i / 20),
                    math.sin(2 * math.pi * i / 20),
                )
                for i in range(10)
            ]
            + [Point(0, 0)]
            + [
                Point(
                    math.cos(2 * math.pi * i / 20),
                    math.sin(2 * math.pi * i / 20),
                )
                for i in range(10, 20)
            ]
        )
        self.assertFalse(
            is_polygon_convex(concave_points), "Failed on concave polygon"
        )

    def test_polygon_with_dent(self):
        points = [
            Point(20, -1),
            Point(19, -5),
            Point(13, -18),
            Point(-11, -19),
            Point(-14, -13),
            Point(-17, -5),
            Point(-20, 12),
            Point(-20, 14),
            Point(-6, 19),
            Point(10, 18),
            Point(18, 7),
            Point(6, 0),
        ]
        self.assertFalse(
            is_polygon_convex(points), "Failed on polygon with dent"
        )

    def test_almost_convex_polygon(self):
        points = [
            Point(0, 0),
            Point(1, 0),
            Point(1, 1),
            Point(1, 2),
            Point(0.75, 1),
            Point(0.5, 1.5),
            Point(0, 1),
        ]
        self.assertFalse(
            is_polygon_convex(points), "Failed on almost convex polygon"
        )


if __name__ == "__main__":
    unittest.main()
