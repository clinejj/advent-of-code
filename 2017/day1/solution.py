import sys


if __name__ == '__main__':

  number_list = ''

  if len(sys.argv) > 2 and sys.argv[1] == '-f':
    with open(sys.argv[2], 'r') as f:
      number_list = f.read()
  else:
    number_list = sys.argv[1]

  number_sum = 0
  #previous_number = number_list[0]
  number_length = len(number_list) - 1
  look = number_length / 2
  print('length: {}'.format(number_length))
  print('list: {}'.format(number_list))

  for i,num in enumerate(number_list):
    # part 1
    # if num == previous_number:
    #     number_sum = number_sum + int(num)
    # previous_number = num
    look_num = number_list[(i+look) % number_length]
    if num == look_num:
        number_sum = number_sum + int(num)


  # if (number_list[0] == number_list[len(number_list) - 1]):
  #     number_sum = number_sum + number_list[0]

  print('sum: {}'.format(number_sum))
