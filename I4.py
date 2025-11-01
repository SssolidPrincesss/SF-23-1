import time

class Phone:
    def __init__(self, brend, model, color, charge):
        self._brend = brend  # защищенный атрибут
        self.__model = model  # приватный атрибут
        self.color = color
        self.charge = charge

    def get_model(self):
        return self.__model
    
    def charging_batery(self):
       print("Charging your batery: ")
       while(self.charge <= 100):
           self.charge += 1
           time.sleep(1)
           print(f"\r{self.charge}% ", end="", flush=True)
            
    
my_phone = Phone("Samsung", "S25 Plus", "blue", 6)
print(f"Phone {my_phone._brend} {my_phone.get_model()}, colored {my_phone.color}")
my_phone.charging_batery()