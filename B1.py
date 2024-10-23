class Vehicle:
    def __init__(self,_brand):
        self.brand=_brand

    def  Start(self):
        return f'{self.brand} is starting'
    
class Car(Vehicle):
    def __init__(self,brandCar,color):
        super().__init__(brandCar)
        self.color=color
    def Start(self):
        SUPERCLASS=super().Start()
        return f'{self.brand} which color {self.color} vehicle is starting'
    
color=input("Nhập màu của chiếc xe: ")
brand=input("Nhập hãng của chiếc xe: ")
car=Car(brand,color)
print(car.brand)
print(car.color)
print(car.Start())