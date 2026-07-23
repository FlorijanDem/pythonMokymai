import math
PI = 3.14
class Shape:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
    
    def calculate_area(self):
        return self.width * self.heigth
    
    def calculate_perimeter(self):
        result = self.width + self.width + self.heigth + self.heigth
        return result

    def display_info(self):
        return f'width: {self.width}, height {self.heigth}, area {self.calculate_area()}, perimeter {self.calculate_perimeter()}'
    
class Rectangle(Shape):
    def __init__(self, width, heigth):
        super().__init__(width, heigth)
        self.name = 'Rectangle'

    def display_info(self):
        return f'{self.name} {super().display_info()}'

class Square(Shape):
    def __init__(self, width, heigth):
        super().__init__(width, heigth)
        self.name = 'Square'

    def display_info(self):
        return f'{self.name} {super().display_info()}'

  
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = "Circle"
    def calculate_area(self):
        area = self.radius * self.radius * PI
        return area
    def calculate_perimeter(self):
        perimeter = 2 * PI * self.radius
        return perimeter
    def display_info(self):
        return f'Circle radius {self.radius}, area {self.calculate_area()}, perimeter {self.calculate_perimeter()}'

class Triangle(Shape):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.name = "Triangle"
        
    def calculate_area(self):
        return super().calculate_area() / 2
    
    def calculate_perimeter(self):
        c_side = math.sqrt(self.width * self.width + self.heigth * self.heigth)
        return self.width + self.heigth + c_side

    def display_info(self):
        return f'Triangle area {self.calculate_area()}, perimeter {self.calculate_perimeter()}'

rect = Rectangle(4, 5)
print(rect.display_info())

squa = Square(4, 4)
print(squa.display_info())

circ = Circle(5)
print(circ.display_info())

triang = Triangle(4, 4)
print(triang.display_info())