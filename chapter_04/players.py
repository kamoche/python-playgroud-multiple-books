players = ['kamoche','sharon','adrian','hannah']
print(players[0:3])
print(players[1:3])
print(players[:4])
print(players[-3:])

print("First three playes on my team")
for player in players[:3]:
	print(player.title())
