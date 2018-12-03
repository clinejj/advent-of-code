import sys

if __name__ == '__main__':

  word_list = []
  matches = []
  found_match = False

  with open(sys.argv[1], 'r') as f:
    for line in f:
      word_list.append(line.strip())

  for word in word_list:
    for second_word in word_list:
      if word == second_word:
        next

      num_diffs = 0
      last_match = 0

      for i in xrange(0, len(word)):
        if word[i] != second_word[i]:
          num_diffs = num_diffs + 1
          last_match = i
        if num_diffs == 2:
          break

      if num_diffs == 1:
        matches.append(word)
        matches.append(second_word)
        matches.append(word.replace(word[last_match], ''))
        found_match = True
        break

    if found_match:
      break

  print('matches: {}'.format(matches))
