import math

def operate(values):
  for i in range(math.ceil(len(values)/4)):
    chunk = values[ i*4 : i*4+4]
    op, x, y, target = [i for i in chunk] 

    if target >= len(values):
      break
    if op == 1:
      values[target] = values[x] + values[y]
    elif op == 2:
      values[target] = values[x] * values[y]
    elif op == 99:
      break
    else:
      print('Something went wrong')
  return values

f = open("day2/input.txt", "r")
values = f.read().split(",")  # no empty space at the end of input file
values = [int(value) for value in values]

for i in range(100):
  for j in range(100):
    tmp = values[:]
    tmp[1] = i
    tmp[2] = j
    output = operate(tmp)[0]
    if output == 19690720:
      print('SUCCESS noun: ', i, ' verb: ', j, ' value: ', output)
      break
