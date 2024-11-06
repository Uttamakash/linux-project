# clock.py

import time
import curses

def display_clock(stdscr):
    # Clear the screen
    stdscr.clear()

    while True:
        # Get the current time
        current_time = time.strftime("%H:%M:%S", time.localtime())

        # Get terminal size and center the time
        height, width = stdscr.getmaxyx()
        x = width // 2 - len(current_time) // 2
        y = height // 2

        # Clear and refresh the screen with new time
        stdscr.clear()
        stdscr.addstr(y, x, current_time)
        stdscr.refresh()

        # Wait for 1 second before updating the time
        time.sleep(1)

# Start the curses application
curses.wrapper(display_clock)
