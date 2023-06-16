
alien_0 = { 'color': 'green', 'points': 5}

#print(alien_0['color'])
#print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print("\nAlien color is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'

print("Alien color now is " + alien_0['color'] + ".")

alien_0['speed'] = 'medium'
print("Original x_position: " + str(alien_0['x_position']) + " current speed: " + alien_0['speed'] + ".")

#Move alien to the right
#Determine how far to move the alien depending on its current speed
alien_current_speed = alien_0['speed']
if alien_current_speed == 'slow':
    x_increment = 1
elif alien_current_speed == 'medium':
    x_increment = 2
else:
    print("It must be a fast alien")
    x_increment = 3


#New alien position
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

print("Removing key points from the dictionary")
del alien_0['points']
print("Current dict: " + str(alien_0))