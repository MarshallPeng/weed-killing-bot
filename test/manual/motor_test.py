import RPi.GPIO as GPIO
from time import sleep

DIR1 = 16
PWM1 = 12
p1 = None


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR1, GPIO.OUT)
    GPIO.setup(PWM1, GPIO.OUT)


def run():
    p1 = GPIO.PWM(PWM1, 100)

    print("Forwards")
    GPIO.output(DIR1, GPIO.HIGH)  # Forwards
    p1.start(50)
    sleep(1)

    print("Pause")
    p1.start(0)
    sleep(1)

    print("backwards")
    GPIO.output(DIR1, GPIO.LOW)  # Backwards
    p1.start(50)
    sleep(1)

    print("End")
    p1.start(0)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':  # Program start from here
    setup()

    try:
        run()
    finally:
        destroy()
