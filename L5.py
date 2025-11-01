#Родительский класс
class Shape:
    #метод-заготовка
    def area(self):
        pass

class Rectangle(Shape):
    #собственный конструктор 
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #Переопределение метода родительского 
    #класса для подсчета площади прямоугльника 
    def area(self):
        return self.width * self.height

class Circle(Shape):
    #собственный конструктор
    def __init__(self, radius):
        self.radius = radius
    #Переопределение метода родительского 
    #класса для подсчета площади круга 
    def area(self):
        return 3.14 * self.radius * self.radius
    
rect = Rectangle(5, 14)
print(rect.area())
circ = Circle(30)
print(circ.area())