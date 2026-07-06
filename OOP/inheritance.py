class vechile:
    def __init__(self, make, name):
        self.make = make
        self.model = name

    def start_engine(self):
        print("Engine started.")
class car(vechile):
    def __init__(self, model):
        self.model = model
    
    def engine_sound(self):
        print("Vroom! Vroom!")

class bike(car):
    def __init__(self, model):
        self.model = model

    def engine_sound(self):    # method overriding
        print("Brrr! Brrr!")


bike1 = bike("Yamaha")
bike1.start_engine()  # from vechile class
bike1.engine_sound()  # from bike class
car1 = car("Toyota")
car1.start_engine()  # from vechile class
car1.engine_sound()  # from car class   