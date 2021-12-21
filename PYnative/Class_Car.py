class Car:
    def __init__(self, make, model, gearbox, doors, color, year):
        self.make = make
        self.model = model
        self.gearbox = gearbox
        self.doors = doors
        self.color = color
        self.year = year

var_make = input("Give me your cars maker! ")
var_model = input(f"Give me {var_make}'s model! ")
var_gearbox = input(f"Is the {var_make} {var_model} manual or automatic? ")
var_doors = input(f'How meny doors your {var_make} {var_model} have? ')
var_color = input(f'What is the color of your {var_make} {var_model}? ')
var_year = input(f'What is the year model of your {var_make} {var_model}? ')



c = Car(var_make, var_model, var_gearbox, var_doors, var_color , var_year)
print(c.make)
print(c.model)
print(c.gearbox)
print(c.doors)
print(c.color)
print(c.year)

