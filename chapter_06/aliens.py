
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

aliens1 = []

for alien in range(30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens1.append(new_alien)

for alien in aliens1[:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'green'
        alien['points'] = 10
        alien['speed'] = 'medium'

#show the first 5 aliens
for alien in aliens1[:5]:
    print(alien)
print("....")


#show the length of the aliens1 list
print("\nThe length of created aliens: " + str(len(aliens1)))