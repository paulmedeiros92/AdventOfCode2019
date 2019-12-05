import matplotlib.pyplot as plt

size = 20000
f = open("day3/input.txt", "r")
paths = f.read().split("\n")  # no empty space at the end of input file
origin = { 'x': int(size/2), 'y': int(size/2), 'count': 0 }
minCollision = { 'x': int(size/2), 'y': int(size/2), 'distance': 0 }
lengths = [0 for i in range(size * 2)]
collisions = []
shortest = 0

def calcDistance(y, x):
  distance = abs((x - origin.get('x'))) + abs((y - origin.get('y')))
  if minCollision.get('distance') == 0 or minCollision.get('distance') > distance:
    minCollision['x'] = x
    minCollision['y'] = y
    minCollision['distance'] = distance

def yMove(delta, field, y, x, char, count):
  for i in range(abs(delta)):
    newY = y + i if delta > 0 else y - i
    count += 1
    content = field[newY][x]
    if content != 0 and content != char:
      calcDistance(newY, x)
      field[newY][x] = 'X'
      if newY != origin.get('y') and x != origin.get('x'):
        collisions.append({ 'y': newY, 'x': x })
        lengths[newY + x] += count
    field[newY][x] = char
  return { 'x': x, 'y': y + delta, 'count': count }

def xMove(delta, field, y, x, char, count):
  for i in range(abs(delta)):
    newX = x + i if delta > 0 else x - i
    count += 1
    content = field[y][newX]
    if content != 0 and content != char:
      calcDistance(y, newX)
      field[y][newX] = 'X'
      if y != origin.get('y') and newX != origin.get('x'):
        collisions.append({ 'y': y, 'x': newX })
        lengths[y + newX] += count
    field[y][newX] = char
  return { 'x': x + delta, 'y': y, 'count': count }

def draw(field, movements, char):
  start = origin.copy()
  for move in movements:
    op = move[0]
    delta = int(move[1:])
    if(op == 'L' or op == 'R'):
      start = xMove(delta if op == 'R' else -delta, field, start.get('y'), start.get('x'), char, start.get('count'))
    elif(op == 'U' or op == 'D'):
      start = yMove(delta if op == 'U' else -delta, field, start.get('y'), start.get('x'), char, start.get('count'))
    else:
      print('Operation is not suported: ', op)

field = [[0 for i in range(size)] for j in range(size)]
chars = [1, 2, 1]

for i, path in enumerate(paths):
  draw(field, path.split(','), chars[i])

for collision in collisions:
  length = lengths[collision.get('y') + collision.get('x')]
  if shortest == 0 or shortest > length:
    shortest = length - 2 # its considering the origin 1 length on each path

print(minCollision)
print(shortest)
plt.imshow(field)
plt.show()