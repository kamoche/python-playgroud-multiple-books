# python tricks
def make_adder(n):
    def add(x):
        return x + n

    return add


class Adder:

    def __init__(self, n):
        self.n = n

    def __call__(self, x, *args, **kwargs):
        return self.n + x


def make_adder_lambda(n):
    return lambda x: x + n


def make_adder_lambda_2(n):
    return lambda x: x + n


plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(str(plus_3(4)))  # = 7
print(str(plus_5(4)))  # = 9
print(str(plus_5(1)))  # = 9

add = Adder(6)
print(str(add(2)))
print(str(add(1)))
