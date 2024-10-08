from POOP1 import Car

car_1 = Car('Chevvy', 'Corvette', 2021, 'Blue')
car_2 = Car('Food','Musting', 2022, 'red')

car_1.drive()
car_2.drive()

car_1.stop()
car_2.stop()

print('------------------Car_2-----------------')
print(car_2.model)
print(car_2.make)
print(car_2.year)
print(car_2.color)

print('------------------Car_1------------------')
print(car_1.model)
print(car_1.make)
print(car_1.year)
print(car_1.color)
