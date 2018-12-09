import sys

if __name__ == '__main__':

  steps = set()
  dependencies = {}

  with open(sys.argv[1], 'r') as f:
    for line in f:
      line_split = line.strip().split(' ')
      steps.add(line_split[1])
      steps.add(line_split[7])

      if line_split[7] not in dependencies:
        dependencies[line_split[7]] = []
      dependencies[line_split[7]].append(line_split[1])

  steps = sorted(steps)
  starting_steps = []

  for step in steps:
    if step not in dependencies:
      starting_steps.append(step)

  starting_steps = sorted(starting_steps)

  print('steps: {}'.format(steps))
  print('dependencies: {}'.format(dependencies))
  print('start at: {}'.format(starting_steps))

  completed_steps = ''
  available_steps = list(starting_steps)

  while len(available_steps) > 0:
    current_step = available_steps.pop(0)
    completed_steps = completed_steps + current_step

    for step in dependencies:
      if current_step in dependencies[step]:
        remaining = list(set(dependencies[step]) - set(completed_steps))
        if len(remaining) == 0:
          available_steps.append(step)

    available_steps.sort()

  # part 1
  print('order: {}'.format(completed_steps))

  # part 2
  base_time = 61
  num_workers = 5
  current_time = 0
  worker_status = {}
  free_workers = []

  for x in xrange(0, num_workers):
    worker_status[x] = []
    free_workers.append(x)

  available_steps = list(starting_steps)
  completed_steps_parallel = []
  in_progress = set()
  remaining_steps = list(set(steps) - set(starting_steps))

  while len(completed_steps_parallel) < len(steps):
    # see if anyone is complete, add to completed
    recent_completions = False
    for worker in worker_status:
      if len(worker_status[worker]) > 0 and worker_status[worker][0] == current_time:
        step = worker_status[worker][1]
        completed_steps_parallel.append(step)
        worker_status[worker] = []
        free_workers.append(worker)
        recent_completions = True

    # find any newly available steps
    if recent_completions:
      for step in remaining_steps:
        remaining = list(set(dependencies[step]) - set(completed_steps_parallel))
        if len(remaining) == 0:
          available_steps.append(step)
      available_steps.sort()

    while len(free_workers) > 0 and len(available_steps) > 0:
      step = available_steps.pop(0)
      if step in remaining_steps: remaining_steps.remove(step)
      worker_status[free_workers[0]] = [current_time + base_time + steps.index(step), step]
      free_workers.pop(0)

    current_time = current_time + 1

  print('parallel order: {}'.format(completed_steps_parallel))
  print('parallel duration: {}'.format(current_time - 1))
