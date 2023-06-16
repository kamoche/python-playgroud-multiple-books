
def greet_users(users):
    for user in users:
        msg = "Hello, " + user.title()
        print(msg)

usernames = ['jack','adi']
greet_users(usernames)