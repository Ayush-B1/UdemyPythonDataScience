class car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def start(self):
        print("The car is starting")

    def stop(self):
        print("The car stopped")

    def breaks(self):
        print("Pressed brake")



my_car = car(name="Maruti Suzuki", model="Swift", year=2017)
print(my_car.name)
print(my_car.model)
print(my_car.year)

my_car.start()

print("car is gonna stop now")
my_car.stop()
