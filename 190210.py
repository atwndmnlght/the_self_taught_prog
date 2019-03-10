class Rectangle:
    def __init__(self, wideth, len):
        self.wideth = wideth
        self.len = len

    def calculate_perimeter(self):
        return self.wideth * self.len

class Square:
    def  __init__(self, wideth):
        self.wideth = wideth

    def calculate_perimeter(self):
        return self.wideth ** 2

rectangle1 = Rectangle(3,2)
square1 = Square(5)
print(rectangle1.calculate_perimeter())
print(square1.calculate_perimeter())
        
