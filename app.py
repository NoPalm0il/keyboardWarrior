from pynput.keyboard import Key, Controller, Listener

import time
import threading


stop = False

#Keyboard listener for keypress -> esc
def on_rel(key):
    if key == Key.ctrl_l:
        return False

def kill():
    global stop
    with Listener(on_release = on_rel) as lis:
        lis.join()
    
    print('ctrl_l pressed')
    stop = True
    wttd.join()
    print('killed thread')


#Printers
def writer():
    keyboard = Controller()

    print('Enter target:\n')
    target = input()

    print('Enter message:\n')
    msg = input()

    print('!!!CHANGE SCREEN TO INPUT YOU WILL HAVE 3 SECS!!!\nPress ENTER to continue...')

    input()

    print('Starting input...')

    for i in range(3):
        print(3-i)
        time.sleep(1)

    for char in "write {}".format(target):
        keyboard.press(char)
        keyboard.release(char)

    keyboard.press(Key.enter)

    global stop
    while True:
        for char in msg:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.002)
        keyboard.press(Key.enter)
        if stop:
            break


wttd = threading.Thread(target=writer, name='thread-writer')

#################==MAIN==#################
def Main():
    wttd.start()
    kill()


Main()
