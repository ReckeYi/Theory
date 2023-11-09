car = {
    "brand": "Форд",
    "model": "Мустанг",
    "year": 1964
}
print(car)
x = car.keys()

print(x)
y = car.items()
print(y)

car["color"] = "белый"
car['model'] = 'KIA'

print(car)
print(x)  # после изменения

y = car.items()
print(y)

car = {
    "brand": "Форд",
    "model": "Мустанг",
    "year": 1964
}
if "model" in car:
    print("Да, 'model' является одним из ключей в словаре thisdict")

for i in car.values():
    print(i)

del car['model']
print(car)

car.pop('brand')
print(car)

car["brand"] = "KIA"
car["color"] = "Silver"
car['model'] = 'Ceed'

print(car)

car = {
    "brand": "KIA",
    "model": "Ceed",
    "year": 1964,
    "color": "Silver"
}
#All Keys:
for x in car:
    print(x)

print('___')

for x in car.keys():
    print(x)
# ALl Values:
print('___')
for x in car:
    print(car[x])

print('___')

for x in car.values():
    print(x)


# ALl Items:
print('___')

for x, y in car.items():
  print(x, y)

mydict = car.copy()
mydict = dict(car)
print(car)
print(mydict)


# Nested dictionaries

my_garage = {
    "car_1" : {
        "brand": "KIA",
        "model": "Ceed",
        "year": 2011,
        "color": "Silver"
    },
    'car_2' : {
        "brand": "FORD",
        "model": "Escape",
        "year": 2002,
        "color": "Silver"
    },
    'car_3' : {
            "brand": "TOYOTA",
            "model": "Hilux",
            "year": 2023,
            "color": "Green"
    }
}

car_1 = {
        "brand": "KIA",
        "model": "Ceed",
        "year": 2011,
        "color": "Silver"
    }

car_2 = {
        "brand": "FORD",
        "model": "Escape",
        "year": 2002,
        "color": "Silver"
    }

car_3 = {
            "brand": "TOYOTA",
            "model": "Hilux",
            "year": 2023,
            "color": "Green"
    }

my_garage_2 = {
    "car_1": car_1,
    "cer_2": car_2,
    "car_3": car_3
}

print(my_garage)
print(my_garage_2)


#fromkeys()
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)