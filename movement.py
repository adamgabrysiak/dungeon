
WIDTH = 160
HEIGHT = 160

def read_state():
	grid = []

	for _ in range(WIDTH):
		row = []

		for _ in range(HEIGHT):
			row.append(0)

		grid.append(row)

	with open("state", "r") as file:
		lines = file.readlines()

	for line in lines:
		if line.startswith("TURN"):
			turn = parse(line)[0]

		if line.startswith("PLAYER_POS"):
			player_x, player_y = parse(line)

		if line.startswith("PLAYER_CARROTS"):
			carrots = parse(line)[0]

		for bonus in ["CRATE", "CARROT"]:
			if line.startswith(bonus):
				x, y = parse(line)
				grid[x][y] = bonus

		for field in ["WHITE_RABBIT", "BROWN_RABBIT", "BLACK_RABBIT"]:
			if line.startswith(field):
				x, y = parse(line)
				grid[x][y] = 5
				try:
					for i in [-5, -4,-3, -2, -1, 0, 1, 2, 3, 4, 5]:
						for j in [-5, -4,-3, -2, -1, 0, 1, 2, 3, 4, 5]:
							grid[x + i][y + j] += 1
					for i in [-4,-3, -2, -1, 0, 1, 2, 3, 4]:
						for j in [-4,-3, -2, -1, 0, 1, 2, 3, 4]:
							grid[x + i][y + j] += 1
					for i in [-3, -2, -1, 0, 1, 2, 3]:
						for j in [- 3, -2, -1, 0, 1, 2, 3]:
							grid[x + i][y + j] += 1
					for i in [ -2, -1, 0, 1, 2]:
						for j in [-2, -1, 0, 1, 2]:
							grid[x + i][y + j] += 1
					for i in [ -1, 0, 1]:
						for j in [-1, 0, 1]:
							grid[x + i][y + j] += 1
				except:
					pass
													
	rabbits = []
	distances = []
	
	for line in lines:			
		for field in ["WHITE_RABBIT", "BROWN_RABBIT", "BLACK_RABBIT"]:
			if line.startswith(field):
				x, y = parse(line)
				rabbits.append((x, y))
				distance = (x - player_x) ** 2 + (y - player_y) ** 2
				distances.append(distance)

	return grid, rabbits, distances, player_x, player_y, carrots

def parse(string):
	array = string[:-1].split("\t")
	array = array[1:]

	for i in range(len(array)):
		array[i] = int(array[i]) - 1 
	
	return array

def display(grid):
	for row in grid:
		print(row)

grid, rabbits, distances, player_x, player_y, carrots = read_state()

index = 0

for i in range(len(distances)):
	if distances[i] < distances[index]:
		index = i

player_range_danger = []

for i in [-1,0,1]:
	for j in [-1,0,1]:
		player_range_danger.append(grid[player_x + i][player_y + j])

player_range_danger.remove(grid[player_x][player_y])

UP = grid[player_x][player_y + 1]
DOWN = grid[player_x][player_y - 1]
LEFT = grid[player_x - 1][player_y]
RIGHT = grid[player_x + 1][player_y]

player_directions = [UP, DOWN, LEFT, RIGHT]

if sum(player_range_danger) > 0:
	if carrots > 0:
		if player_directions[0] >= player_directions[1] and player_directions[0] >= player_directions [2] and player_directions[0] >= player_directions[3]:
			print("THROW_UP")
		elif player_directions[1] >= player_directions[0] and player_directions[1] >= player_directions [2] and player_directions[1] >= player_directions[3]:
			print("THROW_DOWN")
		elif player_directions[2] >= player_directions[0] and player_directions[2] >= player_directions [1] and player_directions[2] >= player_directions[3]:
			print("THROW_LEFT")
		elif player_directions[3] >= player_directions[0] and player_directions[3] >= player_directions [1] and player_directions[3] >= player_directions[2]:
			print("THROW_RIGHT")
	elif player_directions[0] <= player_directions[1] and player_directions[0] <= player_directions [2] and player_directions[0] <= player_directions[3]:
		print("MOVE_UP")
	elif player_directions[1] <= player_directions[0] and player_directions[1] <= player_directions [2] and player_directions[1] <= player_directions[3]:
		print("MOVE_DOWN")
	elif player_directions[2] <= player_directions[0] and player_directions[2] <= player_directions [1] and player_directions[2] <= player_directions[3]:
		print("MOVE_LEFT")
	elif player_directions[3] <= player_directions[0] and player_directions[3] <= player_directions [1] and player_directions[3] <= player_directions[2]:
		print("MOVE_RIGHT")
else:
	print("WAIT")


for columns in range(78):
	grid[columns][42] += 20
	grid[columns][41] += 5
	grid[columns][0] += 20
	grid[columns][1] += 5
for rows in range(43):
 	grid[77][rows] += 20
 	grid[76][rows] += 5
 	grid[0][rows] += 20
 	grid[1][rows] += 5

