# pip install pynput  ## This is a dependencie for the script.

import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Set up the mouse controller
mouse = Controller()

# Configurable parameters
CLICK_DELAY = 0.5  # Time between clicks in seconds
TOGGLE_KEY = KeyCode(char='t')  # Key to toggle the clicker on/off
EXIT_KEY = KeyCode(char='e')  # Key to exit the script

# Clicker state
clicking = False

def toggle_clicker(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking
        if clicking:
            print("Mouse clicker started.")
        else:
            print("Mouse clicker stopped.")
    elif key == EXIT_KEY:
        print("Exiting script.")
        return False

def click_mouse():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(CLICK_DELAY)
        else:
            time.sleep(0.1)

# Start the mouse clicker in a separate thread
from threading import Thread
click_thread = Thread(target=click_mouse)
click_thread.daemon = True
click_thread.start()

# Listen for key presses to toggle clicker or exit
with Listener(on_press=toggle_clicker) as listener:
    listener.join()