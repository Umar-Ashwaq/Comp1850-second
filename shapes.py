import math
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.hypot(self.x,self.y)

    def distance_to(self, other):
        return math.hypot(self.x-other.x, self.y-other.y)
    
class Circle:

    def __init__(self, radius, centre = Point(0.0,0.0)):
        self.radius = radius
        self.centre = centre

    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

    def contains(self, point):
        if self.centre.distance_to(point) <= self.radius:
            return True
        else:
            return False

class Rectangle:

    def __init__(self, width, height, corner = Point(0.0,0.0)):
        self.width = width
        self.height = height
        self.corner = corner

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def contains(self, other):
        if self.corner.x <= other.x <= self.corner.x + self.width and self.corner.y <= other.y <= self.corner.y+self.height:
            return True
        else:
            return False

        