#Создадим класс Car
class Car:
    #Конструктор класса
    def __init__(self, make, model):
        self._make = make #Защищенный атрибут
        self.__model = model #Приватный атрибут
    #метод, который выводит на консоль информацию о машине
    def drive(self):
        print(f"Driving the {self._make}{self.__model}")

#экземпляр класса
my_car = Car("Toyta", "Corolla")
#Получим доступ к защищенному атрибуту
print(my_car._make)
#print(my_car.__model) #А вот так уже нельзя - компилятор ругается на приватность атрибута
#вызов метода
my_car.drive()