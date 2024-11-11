class Car:
    totalCar = 0
    def __init__(self, brand,model):
        self.__brand = brand
        self.__model=model
        Car.totalCar+=1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand;

    @property #decorator making method invokable as property
    def model(self):
        return self.__model;
    
    def set_brand(self,brand):
        self.__brand = brand;
    
    
    @staticmethod #deccorator
    def general_description():
        return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

newCar = Car("Toyota","Corolla")
myCar = ElectricCar("Tesla","Model S","85kWh")

print(isinstance(myCar,Car))
print(isinstance(myCar,ElectricCar))