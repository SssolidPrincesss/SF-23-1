class Phone:
    def __init__(self, brend, model, color):
        self.brend = brend
        self.model = model 
        self.color = color
my_phone = Phone("Samsung", "S25 Plus", "blue")
print(f"Phone {my_phone.brend} {my_phone.model}, colored {my_phone.color}")