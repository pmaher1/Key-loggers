import pynput
import time

from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
import time

mouse = Controller()


def read_file(filename):
    with open(filename, "r") as f:
        #file = f.read()
        for line in f:
            print(line)
            mouse.position = (250, 250)
        # print(file)


read_file("logs.txt")
