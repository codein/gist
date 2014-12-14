import sys
import random
import curses
from datetime import datetime

asdf = ['a','s', 'd', 'f']
jkl = ['j','k', 'l', ';']

current_chars = jkl + asdf
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

    if user_char == actual_char:
        win += 1
    sys.stdout.flush()
curses.endwin()

print 'Total:', total_time
print 'per', (total_time * 1.0)/len(chars)
print (win * 100.0)/len(chars)
