class Shape:
    def area(self):
        raise NotImplementedError("area() method should be implemented by subclasses")
    
    def volume(self):
        raise NotImplementedError("volume() method should be implemented by subclasses")


class TwoDShape(Shape):
    def area(self):
        raise NotImplementedError("area() method should be implemented by 2D subclasses")


class ThreeDShape(Shape):
    def volume(self):
        raise NotImplementedError("volume() method should be implemented by 3D subclasses")


class Square(TwoDShape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Triangle(TwoDShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Cube(ThreeDShape):
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        return self.side_length ** 3


class Cone(ThreeDShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * 3.14159 * (self.radius ** 2) * self.height


square = Square(4)
print(f"Square area: {square.area()}")

triangle = Triangle(4, 6)
print(f"Triangle area: {triangle.area()}")

cube = Cube(3)
print(f"Cube volume: {cube.volume()}")

cone = Cone(3, 5)
print(f"Cone volume: {cone.volume()}")
