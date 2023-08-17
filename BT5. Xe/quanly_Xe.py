class Car:
    def __init__(self,make,model,year,mileage):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=mileage
    
    def increase_mileage(self, distance):
        self.mileage += distance

    def display_infor(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)
        print("Mileage:",self.mileage)

car1 = Car("Toyota", "Camry", 2020, 50000)
car1.increase_mileage(100)
car1.display_infor()
