# def add(*arg):
#     n = 0
#     for i in arg:
#         n = n + i
#     return n 

# print(add(3,4,5,1,2))


# def calculator(n, **kwargs):
#     n = n + kwargs['add']
#     n = n * kwargs['multiply']
#     print(n)
# calculator(2, add= 2, multiply=3)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.year = kw.get('year')
        self.color = kw.get('color')

car = Car(make='Honda', model = 'Civic')
print(car.make)
