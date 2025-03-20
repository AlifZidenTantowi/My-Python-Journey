class car:
  def __init__(self, brand, colour):
    self.brand = brand
    self.colour = colour

  def drive(self):
    print(f"{self.brand} {self.colour} is driving")

class animal:
  def __init__(self, name, sound):
    self.name = name
    self.sound = sound

  def make_sound(self):
    print(f"{self.name} wil make sound like this {self.sound}")

my_animal = animal("dog", "bark bark bark arrrrgrrrg")

my_animal.make_sound()

my_car = car("Civic", "Black")

my_car.drive()
