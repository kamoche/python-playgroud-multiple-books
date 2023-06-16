
class Restaurant():
    """Represents a restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name =  restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is well know for it's " + self.cuisine_type.title + " dishes")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")