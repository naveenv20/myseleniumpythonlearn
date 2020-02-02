"""
Obejct Oriented program
"""


class Car(object):
    """
    object class--- one of primitve class in python
    Car is inheriting
    """

    # Member variables
    wheels = 4

    # here the make and model are instance variables
    def __init__(self, make, model):
        # some thing like constructor
        self.make = make
        self.model = model
        print("Inisde the init method of Car class")

    def getinfo(self):
        print("make of car %s and model is %s and it has %i wheels " % (self.make, self.model, self.wheels))

    def drive(self):
        print("stared")

    def stop(self):
        print("stopped")


class BMW(Car):
    """
    inherited the methoids and varibales from Car class
    """

    def __init__(self):
        #super().__init__(make, model) # calling parent class init method --not mandatory
        print("init BMW init")

    def drive(self):
        print("Overriding the method from BMW")

    def headlights(self):
        print("from BMW headup feature")


c1 = Car('Honda', 'civic')
print(type(c1))
print(c1.make)
c1.getinfo()

c2 = Car('Audi', 'q4')
print(c2.make)
c2.getinfo()
c2.drive()
print("$" * 30)


b = BMW()

b.drive() # overriddem function
b.headlights() # coming from child class function
