class Vehicle:
    def __init__(self, maker, model, color, price):
        self.maker = maker
        self.model = model
        self.color = color
        self.price = price
class IndustrialVehicle(Vehicle):
    def __init__(self, maker, model, color, price, lifting_weight):
        super().__init__(maker, model, color, price)
        self.lifting_weight = lifting_weight

class DailyCars(Vehicle):
    def __init__(self, maker, model, color, price, seats):
        super().__init__(maker, model, color, price)
        self.seats = seats

class Forklift(IndustrialVehicle):
    def __init__(self, maker, model, color, price, lifting_weight):
        super().__init__(maker, model, color, price, lifting_weight)

class Crane(IndustrialVehicle):
    def __init__(self, maker, model, color, price, lifting_weight):
        super().__init__(maker, model, color, price, lifting_weight)

car1 = DailyCars('KIA', 'Ceed', 'SilverGrey', 10000, 5)
forklift1 = Forklift('Ford', 'F150', 'White', 15000, 5)
crane1 = Crane('CAT', "Fuji3000", 'Yellow', 30000, 20)

print(car1.maker, car1.model, car1.color, car1.price, car1.seats)
print(forklift1.maker, forklift1.model, forklift1.price, forklift1.lifting_weight)
print(crane1.maker, crane1.model, crane1.price, crane1.lifting_weight)