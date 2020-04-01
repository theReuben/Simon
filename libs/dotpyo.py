from pynput.keyboard import Key, Listener, Controller as Keyboard
from pynput.mouse import Button, Controller as Mouse
from time import sleep

def click_at(x, y, cm=False):
	mouse = Mouse()
	button = Button.left
	if cm:
		x = int(x * 1366/34.3)
		y = int(y * 768/19.3)
	mouse.position = (x, y)
	mouse.position = (x, y)
	mouse.click(button)

def tap(key):
	keyboard = Keyboard()
	keyboard.press(key)
	sleep(0.1)
	keyboard.release(key)