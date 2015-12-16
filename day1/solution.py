import sys


if __name__ == '__main__':
  
  instructions = ''

  if len(sys.argv) > 2 and sys.argv[1] == '-f':
    with open(sys.argv[2], 'r') as f:
      instructions = f.read()
  else:
    instructions = sys.argv[1]

  current_floor = 0
  first_basement = -1
  num_up = 0
  num_down = 0

  for i,c in enumerate(instructions):
    if c == '(':
      current_floor = current_floor + 1
      num_up = num_up + 1
    elif c == ')':
      current_floor = current_floor - 1
      num_down = num_down + 1
    if (current_floor < 0) and (first_basement < 0):
      first_basement = i + 1

  print('Instructions: {} up, {} down'.format(num_up, num_down))
  print('Current floor: {}'.format(current_floor))
  print('First basement: {}'.format(first_basement))
