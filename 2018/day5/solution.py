import sys
import string

def reduce_code(code):
  has_reaction = True
  while has_reaction:
    previous = ''
    has_reaction = False
    for letter in code:
      if letter.upper() == previous.upper() and letter != previous:
        has_reaction = True
        code = code.replace(previous+letter, '')
        break
      previous = letter

  return code

if __name__ == '__main__':

  code = ''

  with open(sys.argv[1], 'r') as f:
    for line in f:
      code = line.strip()

  has_reaction = True

  reduced_code = reduce_code(code)

  # part 1
  print('final code: {}'.format(reduced_code))
  print('length: {}'.format(len(reduced_code)))

  # part 2
  min_length = len(code)
  min_letter = ''

  for letter in string.lowercase:
    letter_removed = code.replace(letter.upper(), '').replace(letter.lower(), '')
    reduced_letter = reduce_code(letter_removed)
    reduced_length = len(reduced_letter)
    if reduced_length < min_length:
      min_length = reduced_length
      min_letter = letter

  print('removed {}, length was {}'.format(min_letter, min_length))
