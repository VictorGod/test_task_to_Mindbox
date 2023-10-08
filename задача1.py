import math


class Shape:
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * self.radius ** 2

class Triangle(Shape):

  def __init__(self, side1, side2, side3):
    self.sides = [side1, side2, side3]

  def area(self):  
    s = sum(self.sides) / 2
    return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))

  def is_right_triangle(self):
    self.sides.sort()
    return self.sides[0]**2 + self.sides[1]**2 == self.sides[2]**2


import unittest

class TestShapes(unittest.TestCase):

  def test_circle_area(self):
    c = Circle(5)
    self.assertAlmostEqual(c.area(), 78.5398, places=4)

  def test_triangle_area(self): 
    t = Triangle(3,4,5)
    self.assertAlmostEqual(t.area(), 6.0, places=4)

  def test_right_triangle(self):
    t = Triangle(3,4,5) 
    self.assertTrue(t.is_right_triangle())

if __name__ == '__main__':
  unittest.main()
