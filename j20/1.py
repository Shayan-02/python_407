class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        area = (self.side * self.side)
        return area
    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_area(self):
        area = self.width * self.length
        return area
    def calculate_perimeter(self):
        perimeter = (self.width + self.length) * 2
        return perimeter