import curses

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


def run():
    prev_char = None
    while True:
        char = screen.getch()

        if char != prev_char:
            print(f"Command Received: {char}")
            prev_char = char


def destroy():
    GPIO.cleanup()
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    try:
        run()
    finally:
        destroy()
