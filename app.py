from pynput.keyboard import Key, Controller, Listener

import time, threading


stop = False
msg = ''


#Keyboard listener for keypress -> ctr_l
def on_rel(key):
    if key == Key.ctrl_l:
        return False


#listens the keyboard for ctr_l
def listening():
    global stop
    with Listener(on_release = on_rel) as lis:
        lis.join()
        
    kill()


#kills the thread
def kill():
    global stop
    print('ctrl_l pressed')
    stop = True
    wttd.join()
    print('killed thread')


#Prints the input messages
def writer():
    global msg
    keyboard = Controller()

    print('Enter target:\n')
    target = input()

    if target == '':
        print('No target, shuting down...')
        kill()

    print('Enter message:\n')
    msg = input()

    print('!!!CHANGE SCREEN TO INPUT YOU WILL HAVE 3 SECS!!!\nPress ENTER to start timer...')
    input()

    print('Starting input...')
    #3 sec timer
    for i in range(3):
        print(3-i)
        time.sleep(1)

    for char in "write {}".format(target):
        keyboard.press(char)
        keyboard.release(char)

    keyboard.press(Key.enter)


#does the loop to write the message
def loop():
    global stop, msg
    keyboard = Controller()
    while True:
        for char in msg:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.002)
        keyboard.press(Key.enter)
        if stop:
            break


#starts the thread to loop the message
wttd = threading.Thread(target=loop, name='thread-writer1')

#################==MAIN==#################
def Main():
    writer()
    wttd.start()
    listening()
    kill()


Main()
