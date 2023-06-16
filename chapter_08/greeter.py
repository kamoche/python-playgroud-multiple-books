
def greet_user(username):
    """Display a simple greeting"""
    print("Hello! " + username.title())

greet_user("kamoche")


def display_message():
    print("Chapter 8 - Function")

display_message()


def favorite_book(title):
    print("My favorite book is: " + title.title())

favorite_book('My life in crime')


def display_pet(animal_type, name = 'siba'):
    """Display pet information"""
    print("\nI  have a " + animal_type.title())
    print("My " + animal_type + "'s name is "+ name.title())

display_pet(animal_type = 'dog')
