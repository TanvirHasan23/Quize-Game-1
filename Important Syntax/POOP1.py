class Car:
    def __init__(self, model, make, year, color):
        self.model = model     # Variable declared in the constructors known as instance variable
        self.make = make
        self.year = year
        self.color = color

    def drive(self):
        print('The ' + self.model + ' is driving')

    def stop(self):
        print('The ' + self.model + ' is stopped')
