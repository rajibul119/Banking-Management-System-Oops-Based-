class Car:
    def __init__(self,brand,model,price):
        self.brand = brand 
        self.model = model 
        self.price = price 
    
    def print_info(self):
        return f"CAR INFO\nBrand = {self.brand}\nModel = {self.model}\nPrice = {self.price}"
    
c1 = Car("BMW","X30",3000000)
print(c1.print_info())
        