
unconfirmed_users = ['kamoche', 'sharon', 'adrian']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users has been confirmed:")
for user in confirmed_users:
    print("\t" + user.title())