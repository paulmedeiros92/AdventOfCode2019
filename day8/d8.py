LENGTH = 25 * 6
WIDTH = 25
HEIGHT = 6

def findTwos(layer):
  twos = []
  for i, c in enumerate(layer):
    if c == '2':
      twos.append(i)
  return twos

def findColor(layer, twos):
  colors = []
  for i in twos:
    if layer[i] != '2':
      twos.remove(i)
      colors.append({ 'color': layer[i], 'i': i })
  return colors

def fillIn(layer1, colors):
  for color in colors:
    layer1[color['i']] = color['color']
  return layer1


f = open("day8/input.txt", "r")
values = f.read()  # no empty space at the end of input file

layers = []
for i in range(int(len(values) / LENGTH)):
  layers.append(values[LENGTH * i: LENGTH * (i + 1)])

colors = []
twos = findTwos(layers[0])
for layer in layers[1:]:
  colors.extend(findColor(layer, twos))

image = fillIn(list(layers[0]), colors)

for i in range(HEIGHT):
  for x in image[i * WIDTH: (i + 1) * WIDTH]:
    if x == '0' or x == '2':
      print(' ', end = '')
    elif x == '1':
      print('x', end = '')
  print()