import sys

def changePos(direction, location):
  if direction == '<':
    location[0] = location[0]- 1
  elif direction == '>':
    location[0] = location[0] + 1
  elif direction == '^':
    location[1] = location[1] + 1
  elif direction == 'v':
    location[1] = location[1] - 1

  return location

def deliverPackage(pos, houses):
  cur_pos = pos[0], pos[1]
  if cur_pos in houses:
    houses[cur_pos] = houses[cur_pos] + 1
  else:
    houses[cur_pos] = 1

  return houses

if __name__ == '__main__':
  
  directions = ''

  if len(sys.argv) > 2 and sys.argv[1] == '-f':
    with open(sys.argv[2], 'r') as f:
      directions = f.read()
  else:
    directions = sys.argv[1]

  santa = [0, 0]
  robo_santa = [0, 0]
  houses = {}

  houses = deliverPackage(santa, houses)
  houses = deliverPackage(robo_santa, houses)

  for i, c in enumerate(directions):
    if i%2 == 1:
      santa = changePos(c, santa)
      houses = deliverPackage(santa, houses)
    else:
      robo_santa = changePos(c, robo_santa)
      houses = deliverPackage(robo_santa, houses)

  print('Total houses: {}'.format(len(houses)))
