
class Dog:
    """A simple class to model a dog"""

    def __init__(self,name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """Simulate a dog rolling in response to a command"""
        print(self.name.title() + " rolled over")



my_dog = Dog('bosco', 2)

print("My dog's name is " + my_dog.name.title() + "!")
print("My dog is " + str(my_dog.age) + " old")
my_dog.sit()
my_dog.roll_over()
