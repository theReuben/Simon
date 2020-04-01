from pynput.keyboard import Key, Listener, Controller as Keyboard
from pynput.mouse import Button, Controller as Mouse
from time import sleep

def tap(key):
	keyboard = Keyboard()
	keyboard.press(key)
	sleep(0.1)
	keyboard.release(key)

def click_at(x, y):
	mouse = Mouse()
	button = Button.left
	mouse.position = (x, y)
	mouse.click(button)