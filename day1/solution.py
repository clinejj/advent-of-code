import sys

instructions = ''

if len(sys.argv) > 2 and sys.argv[1] == '-f':
  f = open(sys.argv[2], 'r')
  instructions = f.read()
  f.close()
else:
  instructions = sys.argv[1]

current_floor = 0
first_basement = -1
num_up = 0
num_down = 0

for i in range(len(instructions)):
  c = instructions[i]
  if c == '(':
    current_floor = current_floor + 1
    num_up = num_up + 1
  elif c == ')':
    current_floor = current_floor - 1
    num_down = num_down + 1
  if (current_floor < 0) and (first_basement < 0):
    first_basement = i + 1

print('Instructions: ' + str(num_up) + " up, " + str(num_down) + " down")
print('Current floor: ' + str(current_floor))
print('First basement: ' + str(first_basement))
