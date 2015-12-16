import sys

instructions = ''
if len(sys.argv) > 2 and sys.argv[1] == '-f':
  f = open(sys.argv[2], 'r')
  instructions = f.read()
  f.close()
else:
  instructions = sys.argv[1]

num_up = instructions.count('(')
num_down = instructions.count(')')
print('Instructions: ' + str(num_up) + " up, " + str(num_down) + " down")
print('Current floor: ' + str(num_up - num_down))
