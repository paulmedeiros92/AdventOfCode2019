f = open("input.txt", "r")
values = f.read().split("\n")  # no empty space at the end of input file
fuel = 0
total = 0

for value in values:
  fuel = int(int(value) / 3) - 2
  total += fuel
  while int(int(fuel) / 3) >= 2: # read the entire problem for this.... found in the bottom where they specified...
    fuel = int(int(fuel) / 3) - 2
    total += fuel

print(total)