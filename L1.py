#Создадим класс Car
class Car:
    #Конструктор класса
    def __init__(self, make, model):
        self.make = make
        self.model = model 
#экземпляр класса
my_car = Car("Toyta", "Corolla")