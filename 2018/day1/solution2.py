import sys

if __name__ == '__main__':

  start = 0
  frequencies = { start: 1 }
  changes = []
  still_unique = True

  with open(sys.argv[1], 'r') as f:
    for line in f:
      changes.append(line)
  
  while(still_unique):
    for line in changes:
      #print(str(start) + line)
      if line[0] == '-':
        start = start - int(line.split('-')[1])
      elif line[0] == '+':
        start = start + int(line.split('+')[1])
      if start in frequencies:
        still_unique = False
        break
      else:
        frequencies[start] = 1
    print('looping input...{}'.format(len(frequencies)))
  
  print('final: {}'.format(start))
  #print('freqs: {}'.format(frequencies))
