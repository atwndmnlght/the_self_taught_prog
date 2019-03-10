class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        return "I am a shape"

class Square(Shape):
    def  __init__(self, width):
        self.width = width

    def calculate_perimeter(self):
        return self.width ** 2

    def change_size(self, add_width):
        self.width = self.width + add_width

class Rectangle(Shape):
    def __init__(self, width, len):
        self.width = width
        self.len = len

    def calculate_perimeter(self):
        return self.wideth * self.len

sq1 = Square(3)
print(sq1.calculate_perimeter())
sq1.change_size(4)
print(sq1.calculate_perimeter())


sq2 = Square(7)
re2 = Rectangle(2,9)
print(sq2.what_am_i())
print(re2.what_am_i())

class Horse:
    def __init__(self,weight,color, owner_name):
        self.weight = weight
        self.color = color
        self.owner_name = owner_name

class Rider:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rider1 = Rider("Takeuchi", 32)
horse1 = Horse(100, "black", rider1)
print(horse1.owner_name.name)
