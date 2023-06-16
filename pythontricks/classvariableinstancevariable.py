class Dog:
    num_legs = 4  # <- Class variable

    def __init__(self, name):
        self.name = name  # <- Instance variable


jack = Dog('Jack')
jill = Dog('Jill')

res = jack.name, jill.name
# ('Jack', 'Jill')

legs = jack.num_legs, jill.num_legs
# (4, 4)

"""Instance variables are specific to
each object instance and are created when the __init__ constructor
runs—they don’t even exist on the class itself."""


class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1
