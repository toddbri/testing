class Vehicle(object):
    count = 0
    def __init__(self, make, model,year):
        Vehicle.count +=1
        if Vehicle.count == 10:
            print "Congratulations, you are the 10th car today"
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print "%s %s %s" % (self.year, self.make, self.model)


car = Vehicle('Nissan','Leaf','2015')

print car.make, car.model, car.year
car.print_info()

for i in range(20):
    Vehicle('1','2','3')
