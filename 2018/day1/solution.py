import sys

if __name__ == '__main__':

  start = 0

  with open(sys.argv[1], 'r') as f:
    for line in f:
      print(str(start) + line)
      if line[0] == '-':
        start = start - int(line.split('-')[1])
      elif line[0] == '+':
        start = start + int(line.split('+')[1])
  
  print('final: {}'.format(start))
