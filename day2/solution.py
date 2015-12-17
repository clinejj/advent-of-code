import sys

def getSurfaceArea(dimensions):
  if (len(dimensions) < 3): return
  return 2*dimensions[0]*dimensions[1] + 2*dimensions[1]*dimensions[2] + 2*dimensions[0]*dimensions[2]

if __name__ == '__main__':
  
  dimension_list = ''

  if len(sys.argv) > 2 and sys.argv[1] == '-f':
    with open(sys.argv[2], 'r') as f:
      dimension_list = f.read()
  else:
    dimension_list = sys.argv[1]

  total = 0

  for package in dimension_list.splitlines():
    package_sizes = map(int, package.split('x'))
    surface_area = getSurfaceArea(package_sizes)
    package_sizes.remove(max(package_sizes))
    extra = package_sizes[0] * package_sizes[1]
    total = total + surface_area + extra

  print('Total: {}'.format(total))
