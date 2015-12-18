import sys

if __name__ == '__main__':
  
  directions = ''

  if len(sys.argv) > 2 and sys.argv[1] == '-f':
    with open(sys.argv[2], 'r') as f:
      directions = f.read()
  else:
    directions = sys.argv[1]

  cur_x = 0
  cur_y = 0
  repeat_houses = 0
  houses = {}

  # Deliver the package
  cur_pos = cur_x, cur_y
  if cur_pos in houses:
    houses[cur_pos] = houses[cur_pos] + 1
  else:
    houses[cur_pos] = 1

  for c in directions:
    #Move
    if c == '<':
      cur_x = cur_x - 1
    elif c == '>':
      cur_x = cur_x + 1
    elif c == '^':
      cur_y = cur_y + 1
    elif c == 'v':
      cur_y = cur_y - 1
      
    # Deliver the package
    cur_pos = cur_x, cur_y
    if cur_pos in houses:
      houses[cur_pos] = houses[cur_pos] + 1
    else:
      houses[cur_pos] = 1
    

  for house in houses.keys():
    if houses[house] > 1:
      repeat_houses = repeat_houses + 1

  print('Total houses: {}'.format(len(houses)))
  print('Repeat houses: {}'.format(repeat_houses))
