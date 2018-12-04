import sys
import time
from datetime import datetime

if __name__ == '__main__':

  squares = {}
  count_claims = 0
  log_entries = []

  with open(sys.argv[1], 'r') as f:
    for entry in f:
      log_entries.append(entry.strip())

  log_entries.sort()

  current_guard = ''
  start_date = ''
  guard_total_minutes = {}
  guard_minute_count = {}

  for entry in log_entries:
    entry_split = entry.replace('[', '').replace(']', '').split(' ')
    date_split = entry_split[0].split('-')
    time_split = entry_split[1].split(':')
    if 'begins shift' in entry:
      current_guard = entry_split[3]
    elif 'falls asleep' in entry:
      start_date = datetime(int(date_split[0]),int(date_split[1]),int(date_split[2]),int(time_split[0]),int(time_split[1]))
    elif 'wakes up' in entry:
      end_date = datetime(int(date_split[0]),int(date_split[1]),int(date_split[2]),int(time_split[0]),int(time_split[1]))
      time_difference = end_date - start_date
      diff_minutes = int(time_difference.total_seconds()/60)
      if current_guard in guard_total_minutes:
        guard_total_minutes[current_guard] = guard_total_minutes[current_guard] + diff_minutes
      else:
        guard_total_minutes[current_guard] = diff_minutes

      if current_guard not in guard_minute_count:
        guard_minute_count[current_guard] = []
      guard_minute_count[current_guard].append((start_date, end_date))

  max_guard = ''
  max_guard_count = 0
  for guard in guard_total_minutes:
    if guard_total_minutes[guard] > max_guard_count:
      max_guard = guard
      max_guard_count = guard_total_minutes[guard]

  # find the guard that's asleep the most, and when they're most asleep
  time_sleeps = {}
  max_time = ''
  max_time_value = 0
  for x in xrange(0, 60):
    time_sleeps[x] = 0
    for range in guard_minute_count[max_guard]:
      minute_date = datetime(range[0].year, range[0].month, range[0].day, 0, x)
      if minute_date >= range[0] and minute_date < range[1]:
        time_sleeps[x] = time_sleeps[x] + 1
    if time_sleeps[x] > max_time_value:
      max_time = x
      max_time_value = time_sleeps[x]

  #find the guard that's most asleep on the same minute
  time_sleeps = {}
  max_guard_overall = ''
  max_time_overall_name = ''
  max_time_overall = 0
  for x in xrange(0, 60):
    time_sleeps = {}
    for guard in guard_total_minutes:
      time_sleeps[guard] = 0
      for range in guard_minute_count[guard]:
        minute_date = datetime(range[0].year, range[0].month, range[0].day, 0, x)
        if minute_date >= range[0] and minute_date < range[1]:
          time_sleeps[guard] = time_sleeps[guard] + 1
      if time_sleeps[guard] > max_time_overall:
        max_guard_overall = guard
        max_time_overall_name = x
        max_time_overall = time_sleeps[guard]



  print('max guard is {}, minute is {}, value is {}'.format(max_guard, max_time, int(max_guard.replace('#','')) * max_time))
  print('overall guard is {}, minute is {}, value is {}'.format(max_guard_overall, max_time_overall_name, int(max_guard_overall.replace('#','')) * max_time_overall_name))
