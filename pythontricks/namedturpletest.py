from collections import namedtuple
from sys import getsizeof
from typing import NamedTuple

Car = namedtuple('Car', 'color mileage')
Car2 = namedtuple('Car', ['color', 'mileage'])

my_car = Car('red', 3812.4)

my_car.color
my_car.mileage


class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


c = MyCarWithMethods('red', 1234)

c.hexcolor()
# '#ff0000'


ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))

print(ElectricCar('red', 1234, 45.0))

my_car._asdict()


my_car._replace(color='blue')


Car._make(['red', 999])

p1 = namedtuple('Point', 'x y z')(1, 2, 3)

p2 = (1, 2, 3)

print(getsizeof(p1))

print(getsizeof(p2))


class Car6(NamedTuple):
    color: str
    mileage: float
    automatic: bool

car6 = Car('red', 3812.4, True)

# Type annotations are not enforced without
# a separate type checking tool like mypy:
Car6('red', 'NOT_A_FLOAT', 99)