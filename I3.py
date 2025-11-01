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
            
class SmartPhone(Phone):
    def __init__(self, brend, model, color, charge, os, camera_mp, storage_gb):
        super().__init__(brend, model, color, charge)
        self.os = os
        self.camera_mp = camera_mp
        self.storage_gb = storage_gb
        self.apps = []
    
    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"App '{app_name}' installed successfully!")
    
    def charging_batery(self):
        print("Fast charging activated: ")
        while self.charge < 100:
            self.charge += 2
            time.sleep(0.1)
            print(f"\r{self.charge}% ", end="", flush=True)
        print("\nFast charging complete!")
    
    def take_photo(self):
        print(f"Photo taken with {self.camera_mp}MP camera!")
        time.sleep(0.5)
    
    def browse_internet(self, website):
        print(f"Opening {website}...")
        time.sleep(1)
        print("Page loaded successfully")

my_smartphone = SmartPhone("iPhone", "15 Pro", "black", 20, "iOS", 48, 256)
print(f"SmartPhone: {my_smartphone.brend} {my_smartphone.model}")
print(f"OS: {my_smartphone.os}, Camera: {my_smartphone.camera_mp}MP")
my_smartphone.charging_batery()
my_smartphone.install_app("WhatsApp")
my_smartphone.take_photo()
my_smartphone.browse_internet("google.com")
print()