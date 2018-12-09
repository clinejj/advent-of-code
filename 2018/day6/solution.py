import sys

def distances(point, coords):
  distance_list = []
  for coord in coords:
    distance = abs(coord[0] - point[0]) + abs(coord[1] - point[1])
    distance_list.append(distance)
  return distance_list

if __name__ == '__main__':

  coords = []
  smallest_x = sys.maxint
  smallest_y = sys.maxint
  largest_x = 0
  largest_y = 0

  with open(sys.argv[1], 'r') as f:
    for line in f:
      line_split = line.strip().split(',')
      x = int(line_split[0].strip())
      y = int(line_split[1].strip())
      if x > largest_x:
        largest_x = x
      if y > largest_y:
        largest_y = y
      if x < smallest_x:
        smallest_x = x
      if y < smallest_y:
        smallest_y = y
      coords.append((x, y))

  area_sizes = {}
  for coord in coords:
    area_sizes[coord] = 0

  max_distance = 10000
  max_distance_size = 0

  for x in xrange(smallest_x, largest_x):
    for y in xrange(smallest_y, largest_y):
      # calc distances for each point
      distance_list = distances((x,y), coords)
      if sum(distance_list) < max_distance:
        max_distance_size = max_distance_size + 1

      # if only one closest, store into area_sizes
      min_distance = min(distance_list)
      distance_index = distance_list.index(min_distance)
      if distance_list.count(min_distance) == 1:
        area_sizes[coords[distance_index]] = area_sizes[coords[distance_index]] + 1

  # part 1
  print('largest area: {}'.format(max(area_sizes.values())))
  # part 2
  print('region with max_distance < {}: {}'.format(max_distance, max_distance_size))
