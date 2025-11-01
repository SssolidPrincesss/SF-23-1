#Создадим класс Car
class Car:
    #Конструктор класса
    def __init__(self, make, model):
        self.make = make
        self.model = model 
    #метод, который выводит на консоль информацию о машине
    def drive(self):
        print(f"Driving the {self.make}{self.model}")

#экземпляр класса
my_car = Car("Toyta", "Corolla")
#вызов метода
my_car.drive()