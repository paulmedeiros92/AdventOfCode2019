rawInput = input()
ranges = rawInput.split('-')
count = 0
doubles = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']
triples = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999']

def twoAdjacent(num):
  strNum = str(num)
  for i, double in enumerate(doubles):
    if double in strNum and triples[i] not in strNum:
      return True
  return False

def neverDecrease(num):
  strNum = str(num)
  for i, digit in enumerate(strNum):
    if i !=5 and int(digit) > int(strNum[i + 1]):
      return False
  return True

for i in range(int(ranges[0]), int(ranges[1])):
  if twoAdjacent(i) and neverDecrease(i):
    count += 1

print(count)