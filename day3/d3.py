import matplotlib.pyplot as plt

f = open("day3/input.txt", "r")
paths = f.read().split("\n")  # no empty space at the end of input file
origin = { 'x': 1000, 'y': 1000 }
minCollision = { 'x': 1000, 'y': 1000, 'distance': 0 }

def calcDistance(x, y):
  distance = (x - origin.get('x')) + (y - origin.get('y'))
  if minCollision.get('distance') == 0 | minCollision.get('distance') > distance:
    minCollision = { 'x': x, 'y': y, 'distance': distance } 

def yMove(delta, field, x, y, char):
  for i in range(delta):
    content = field[x][y + i]
    if content == char:
      calcDistance(x, y + i)
      field[x][y + i] = 'X'
    field[x][y + i] = char
  return { 'x': x, 'y': y + i }

def xMove(delta, field, x, y, char):
  for i in range(delta):
    content = field[x + i][y]
    if content == char:
      calcDistance(x + i, y)
      field[x + i][y] = 'X'
    field[x + i][y] = char
  return { 'x': x + i, 'y': y}

def draw(field, movements, char):
  start = origin.copy()
  for move in movements:
    op = move[0]
    delta = move[1:]
    if(op == 'L' | op =='R'):
      start = xMove(delta if op == 'R' else -delta, field, start.get('x'), start.get('y'), char)
    elif(op == 'U' | op == 'D'):
      start = yMove(delta if op == 'U' else -delta, field, start.get('x'), start.get('y'), char)
    else:
      print('Operation is not suported: ', op)
    # if x is found find distance and cache min distance


field = [[0 for i in range(2000)] for j in range(2000)]
chars = ['A', 'B']

for i, path in enumerate(paths):
  draw(field, path.split(','), chars[i])

plt.imshow(data)
plt.show()