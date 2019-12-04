f = open("day2/input.txt", "r")
values = f.read().split(",")  # no empty space at the end of input file

for i in range(len(values)/4):
  chunk = values[i: i+3]
  if 99 in chunk:
    break

  if values[op] == 1:
    values[target] = values[x] + values[y]
  
  if values[op] == 2:
    values[target] = values[x] * values[y]

print(values)  