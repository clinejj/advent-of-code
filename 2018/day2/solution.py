import sys

if __name__ == '__main__':

  num_words_with_doubles = 0
  num_words_with_triples = 0

  with open(sys.argv[1], 'r') as f:
    for line in f:
      letter_map = {}

      for letter in line:
        if letter in letter_map:
          letter_map[letter] = letter_map[letter] + 1
        else:
          letter_map[letter] = 1
      letter_values = set(letter_map.values())

      if 2 in letter_values:
        num_words_with_doubles = num_words_with_doubles + 1
      if 3 in letter_values:
        num_words_with_triples = num_words_with_triples + 1
  
  print('checksum: {} x {} = {}'.format(num_words_with_doubles, num_words_with_triples, num_words_with_doubles*num_words_with_triples))
