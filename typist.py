#!/usr/bin/env python

import sys
import random
import curses
import json

from datetime import datetime

asdf = ['a','s', 'd', 'f']
jkl = ['j','k', 'l', ';']
g = ['g']
h = ['h']
run_from_vikky = ['r','f','v']
uncle_joes_mad = ['u','j','m']
to_get_betty = ['t','g','b']
you_have_nothing = ['y','h','n']
index_finger_left = ['f','r','v','t','g','b']
index_finger_right = ['u','j','m','n','h','y']

lesson1 = jkl + asdf + g + h
lesson2 = g + h + run_from_vikky + uncle_joes_mad
lesson3 = index_finger_right + index_finger_left
lesson4 = index_finger_right + index_finger_left + asdf + jkl

progress_file = file('progress.json', 'r+')
try:
    progress = json.load(progress_file)
except ValueError:
    progress = {}

progress_file.close()

current_chars = lesson4
REPEATS = 3
chars = current_chars * REPEATS
[random.shuffle(chars) for i in xrange(REPEATS*2)]

total_time = 0
win = 0
stdscr = curses.initscr()
stdscr.keypad(1)
is_first = True
for actual_char in chars:
    start_time = datetime.now()
    stdscr.addstr(0,0,actual_char)
    user_char = chr(stdscr.getch())
    # stdscr.addstr("\n")
    stdscr.refresh()
    if is_first:
        is_first = False
    else:
        delta = datetime.now() - start_time
        total_time  += delta.total_seconds()

    if actual_char not in progress:
        progress[actual_char] = {
            'hit': 0,
            'miss': 0
        }

    if user_char == actual_char:
        progress[actual_char]['hit'] += 1
        win += 1
    else:
        progress[actual_char]['miss'] += 1

    sys.stdout.flush()
curses.endwin()

progress_file = file('progress.json', 'w+')
json.dump(progress, progress_file)
progress_file.close()

print 'Total:', total_time
print 'Time:', (total_time * 1.0)/len(chars)
print (win * 100.0)/len(chars)
