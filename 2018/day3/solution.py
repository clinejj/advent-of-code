import sys

if __name__ == '__main__':

  squares = {}
  count_claims = 0
  unique_claims = set()

  with open(sys.argv[1], 'r') as f:
    for claim in f:
      count_claims = count_claims + 1
      claim_data = claim.split('@')
      claim_id = claim_data[0].strip()
      unique_claims.add(claim_id)

      space_details = claim_data[1].strip().split(':')

      position = space_details[0].strip().split(',')
      left = int(position[0])
      top = int(position[1])

      size = space_details[1].strip().split('x')
      width = int(size[0])
      height = int(size[1])

      overlapped_claims = []
      for x in xrange(1, width+1):
        for y in xrange(1, height+1):
          location = (left + x, top + y)
          if location in squares:
            squares[location].append(claim_id)
            overlapped_claims.extend(squares[location])
          else:
            squares[location] = [claim_id]

      if len(overlapped_claims) > 0:
        unique_claims = unique_claims.difference(set(overlapped_claims))

  total_overlaps = 0
  for value in squares.values():
    if len(value) > 1:
      total_overlaps = total_overlaps + 1

  print('processed {} claims, total overlapped squares: {}'.format(count_claims, total_overlaps))
  print('unique claims: {}'.format(unique_claims))
