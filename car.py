class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has " + str(self.odometer_reading) + "miles on it.")
    def update_odometer(self):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model,year)
        self.battery_size = 70
    def describe_battery(self):
        print("this car has a" + str(self.battery_size) + "-kWh battery." )
my_tesla = ElectricCar('tesla', 'model s', '2018')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()