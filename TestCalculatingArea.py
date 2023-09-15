import math
import unittest
from CalculatingArea import Circle, Triangle


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertEqual(circle.get_square(), 25 * math.pi)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-5)


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.get_square(), 6.0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5)

    def test_non_positive_sides(self):
        with self.assertRaises(ValueError):
            Triangle(0, 4, 5)

    def test_is_rectangular_triangle(self):
        # Тест на прямоугольный треугольник
        right_triangle = Triangle(3, 4, 5)
        self.assertEqual(right_triangle.is_rectangular_triangle(), "Треугольник прямоугольный")

        # Тест на не прямоугольный треугольник
        non_right_triangle = Triangle(3, 4, 6)
        self.assertEqual(non_right_triangle.is_rectangular_triangle(), "Треугольник не прямоугольный")


if __name__ == '__main__':
    unittest.main()
