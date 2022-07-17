class car:
    def __init__(self_, body, engine, tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def milage (self):
        print("milage of this car")




#inheritance

    #pass means not declaring anything

 c = car("metal", "aero", "street")
#making objects inside car class
print(c)

class toyota(car):
    pass

t=toyota("metal1", "aero1", "street1")
print(t)


