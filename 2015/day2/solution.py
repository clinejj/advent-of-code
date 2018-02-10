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

  total_paper = 0
  total_ribbon = 0

  for package in dimension_list.splitlines():
    package_sizes = map(int, package.split('x'))
    surface_area = getSurfaceArea(package_sizes)
    volume = package_sizes[0] * package_sizes[1] * package_sizes[2]
    package_sizes.remove(max(package_sizes))
    extra = package_sizes[0] * package_sizes[1]
    extra_perimeter = 2*package_sizes[0] + 2*package_sizes[1]
    total_paper = total_paper + surface_area + extra
    total_ribbon = total_ribbon + extra_perimeter + volume

  print('Total Paper: {}'.format(total_paper))
  print('Total Ribbon: {}'.format(total_ribbon))
