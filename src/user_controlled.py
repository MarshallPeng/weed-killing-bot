import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes

from src.components.drive_train import DriveTrain

device = InputDevice("/dev/input/event0")  # my keyboard

GPIO.setmode(GPIO.BCM)
drive_train = DriveTrain()


def run():
    char = None
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            char = ecodes.ecodes[categorize(event).keycode]

        if char is ecodes.KEY_Q:
            print("break")
            drive_train.stop()
            break
        elif char is ecodes.KEY_UP:
            print("forward")
            drive_train.forwards()
        elif char is ecodes.KEY_DOWN:
            print("backwards")
            drive_train.backwards()
        elif char is ecodes.KEY_LEFT:
            print("left")
            drive_train.left()
        elif char is ecodes.KEY_RIGHT:
            print("right")
            drive_train.right()
        elif char is ecodes.KEY_ENTER:  # the "ok" button in the middle, not the actual "enter" key
            print("stop")
            drive_train.stop()


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        run()
    finally:
        destroy()
