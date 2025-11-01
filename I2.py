import time

class Phone:
    def __init__(self, brend, model, color, charge):
        self.brend = brend
        self.model = model 
        self.color = color
        self.charge = charge

    def charging_batery(self):
       print("Charging your batery: ")
       while(self.charge <= 100):
           self.charge += 1
           time.sleep(1)
           print(f"\r{self.charge}% ", end="", flush=True)
            
    
my_phone = Phone("Samsung", "S25 Plus", "blue", 6)
print(f"Phone {my_phone.brend} {my_phone.model}, colored {my_phone.color}")
my_phone.charging_batery()