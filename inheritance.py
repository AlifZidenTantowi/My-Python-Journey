class Vehicle:
  def __init__(self, brand, years):
    self.brand = brand
    self.years = years

  def my_vehicle(self):
    print(f"your vehicle brand is {self.brand} and it produce in {self.years} year")

class Car(Vehicle):
  def __init__(self, brand, years, model):
    super().__init__(brand, years)
    self.model = model
  def car_model(self):
    print(f"model car and {self.model}")

my_vehicel = Vehicle("Civic", "2025")
my_vehicel.my_vehicle()

my_car = Car("Civic", "2025", "sedan")
my_car.car_model()

