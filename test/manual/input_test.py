from evdev import InputDevice, categorize, ecodes

device = InputDevice("/dev/input/event0")  # my keyboard
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        char = ecodes.ecodes[categorize(event).keycode]
        print(char, categorize(event).keycode)
        print(type(char), type(categorize(event).keycode))
        print(char is ecodes.KEY_Q)

