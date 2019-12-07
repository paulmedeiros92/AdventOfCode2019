import math

def determineOP(strOP):
  op = [0, 0, 0, 33]
  mLen = len(strOP) - 1
  for i in range(mLen, -1, -1):
    if i == mLen - 4:
      op[0] = int(strOP[i])
    elif i == mLen - 3:
      op[1] = int(strOP[i])
    elif i == mLen - 2:
      op[2] = int(strOP[i])
    elif i == mLen:
      op[3] = int(strOP[i - 1] + strOP[i]) if mLen > 0 else int(strOP[i])
  return op

def getOperands(num, values, i):
  operands = [i + num]
  for operand in range(num):
    operands.append(values[i + operand])
  return operands

def operate(values):
  i = 0
  while i < len(values):
    a, b, c, opcode = determineOP(str(values[i]))
    i += 1
    if opcode == 1:
      i, first, second, target = getOperands(3, values, i)
      summ = (first if c else values[first]) + (second if b else values[second]) 
      values[target] = summ 
    elif opcode == 2:
      i, first, second, target = getOperands(3, values, i)
      product = (first if c else values[first]) * (second if b else values[second])
      values[target] = product
    elif opcode == 3:
      i, target = getOperands(1, values, i)
      x = int(input('Input: '))
      values[target] = x
    elif opcode == 4:
      i, target = getOperands(1, values, i)
      print(target if c else values[target])
    elif opcode == 5:
      i, first, second = getOperands(2, values, i)
      jump = (first != 0 if c else values[first] != 0)
      if jump:
        i = second if b else values[second]
    elif opcode == 6:
      i, first, second = getOperands(2, values, i)
      jump = (first == 0 if c else values[first] == 0)
      if jump:
        i = second if b else values[second]
    elif opcode == 7:
      i, first, second, target = getOperands(3, values, i)
      less = (first if c else values[first]) < (second if b else values[second])
      values[target] = 1 if less else 0
    elif opcode == 8:
      i, first, second, target = getOperands(3, values, i)
      equal = (first if c else values[first]) == (second if b else values[second])
      values[target] = 1 if equal else 0
    elif opcode == 99:
      break
    else:
      print('Something went wrong')
  return values

f = open("day5/input.txt", "r")
values = f.read().split(",")  # no empty space at the end of input file
values = [int(value) for value in values]

operate(values)
