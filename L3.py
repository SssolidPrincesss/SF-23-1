#Все тот же класс, что и раньше
class Car:
    #Конструктор класса
    def __init__(self, make, model):
        self.make = make
        self.model = model 
    #метод, который выводит на консоль информацию о машине
    def drive(self):
        print(f"Driving the {self.make}{self.model}")

class ElectricCar(Car):
    #Конструктор класса
    def __init__(self, make, model, battery_capacity):
        #Заимствуем свойства родительского класса
        super().__init__(make, model)
        #Новый параметр дочернего класса
        self.battery_capacity =  battery_capacity
    #метод для вывода марки, модели и емкости
    def charge(self):
        print(f"Charging the {self.make}{self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()