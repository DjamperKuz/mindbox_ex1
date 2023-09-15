import math
from abc import abstractmethod, ABC


class GeomSquare(ABC):
    @abstractmethod
    def get_square(self):
        pass


class Circle(GeomSquare):
    def __init__(self, radius: float):
        self.radius = radius

    def get_square(self):
        """Вычисляет площадь круга по радиусу."""
        if self.radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        area = math.pi * self.radius ** 2
        return area


class Triangle(GeomSquare):
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_square(self):
        """Вычисляет площадь треугольника по трём сторонам с использованием формулы Герона."""
        if any(side <= 0 for side in [self.side1, self.side2, self.side3]):
            raise ValueError("Все стороны треугольника должны быть положительными числами")
        s = (self.side1 + self.side2 + self.side3) / 2  # Полупериметр треугольника
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def is_rectangular_triangle(self):
        """Проверяет, является ли треугольник прямоугольным с помощью теоремы Пифагора."""
        sides = sorted([self.side1, self.side2, self.side3])
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            return "Треугольник прямоугольный"
        else:
            return "Треугольник не прямоугольный"
