class Point:
  def __init__(self, x, y, slopeX, slopeY):
    self.x = x
    self.y = y
    if slopeY == 0:
      self.slopeX = 1 if slopeX > 0 else -1
    else:
      self.slopeX = slopeX
    if slopeX == 0:
      self.slopeY = 1 if slopeY > 0 else -1
    else:
      self.slopeY = slopeY
    self.slopeY
    self.distance = abs(slopeX) + abs(slopeY)
    self.visible = 0

def findAllAsteroids(rows):
  points = []
  for y, row in enumerate(rows):
    for x, char in enumerate(row):
      if char == '#':
        points.append(Point(x, y, x, y))
  return points

def findFactors(x):
  factors = []
  for i in range(1, x + 1):
    if x % i == 0:
      factors.append(i)
  return factors

def simpleForm(node):
  intersection = [ value for value in findFactors(abs(node.slopeX)) if value in findFactors(abs(node.slopeY)) and value != 1]
  intersection.sort(reverse=True)
  if len(intersection) > 0:
    node.slopeX = int(node.slopeX / intersection[0])
    node.slopeY = int(node.slopeY / intersection[0])
  return node

def findDistancesFrom(origin, asteroids):
  distances = []
  for asteroid in asteroids:
    rock = simpleForm(Point(asteroid.x, asteroid.y, asteroid.x - origin.x, asteroid.y - origin.y))
    similar = next((z for z in distances if z.slopeX == rock.slopeX and z.slopeY == rock.slopeY), None)
    if similar != None and similar.distance > rock.distance:
      distances.remove(similar)
      distances.append(rock)
    elif similar == None:
      distances.append(rock)
  return distances

f = open("day10/input.txt", "r")
rows = f.read().split("\n")

asteroids = findAllAsteroids(rows)
bestHome = asteroids[0]
for asteroid in asteroids:
  others = asteroids[:]
  others.remove(asteroid)
  distances = findDistancesFrom(asteroid, others)
  asteroid.visible = len(distances)
  # print("Asteroid: x = ", asteroid.x, ", and y = ", asteroid.y, "visible = ", asteroid.visible)
  if asteroid.visible > bestHome.visible:
    bestHome = asteroid

print("BestHome: x = ", bestHome.x, ", and y = ", bestHome.y, "visible = ", bestHome.visible)
