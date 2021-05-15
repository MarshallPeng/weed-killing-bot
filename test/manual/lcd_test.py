from signal import signal, SIGTERM, SIGHUP, pause

from rpi_lcd import LCD

lcd = LCD()


# MultiThread the display
def safe_exit(signum, frame):
    exit(1)


signal(SIGTERM, safe_exit)
signal(SIGHUP, pause)

try:
    lcd.text("Hello", 1)
    lcd.text("World", 2)

    pause()

finally:
    lcd.clear()
