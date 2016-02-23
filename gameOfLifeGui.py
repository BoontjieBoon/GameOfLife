import gameOfLife as g
import curses
from time import sleep
from itertools import product
from random import randint


if __name__ == '__main__':
    try:
        # initialise curses
        stdscr = curses.initscr()

        # turn off normal terminal functionality
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        stdscr.keypad(1)

        # set colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # set terminal color
        stdscr.bkgd(curses.color_pair(2))
        stdscr.refresh()

        width = 20
        height = 20

        # set game window color
        world = curses.newwin(height + 2, width + 2, 0, 0)
        world.bkgd(curses.color_pair(1))
        world.refresh()

        # create game and populate it with 50 random cells
        game = g.GameOfLife()
        for i in range(50):
            game.set_alive(randint(1, width), randint(1, height))

        # curses' getch() function usually pauses and waits
        # for input, this changes the behaviour to not pause
        stdscr.nodelay(1)

        # loop until 'q' is pressed
        while True:
            # write '@' characters for living cells
            # and '.' for dead ones
            for x, y in product(range(1, width + 1), range(1, height + 1)):
                if game.is_alive(x, y):
                    world.addch(int(y), int(x), '@')
                else:
                    world.addch(y, int(x), '.')
            # update the display
            world.refresh()

            # wait a second
            sleep(1)
            # next generation
            game.tick()

            # check if the q was pressed to quit
            c = stdscr.getch()
            if c == ord('q'):
                break
    finally:
        # return the terminal to its previous state
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()
