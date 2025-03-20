class car:
  def __init__(self, brand, colour):
    self.brand = brand
    self.colour = colour

  def drive(self):
    print(f"{self.brand} {self.colour} is driving")

my_car = car("Civic", "Black")

my_car.drive()
