from __future__ import division
import time
from sys import argv
from time import sleep
from pynput.keyboard import Key, Listener, Controller as Keyboard
from pynput.mouse import Button, Controller as Mouse
from datetime import datetime as dt

def tap(key):
	keyboard.press(key)
	sleep(0.1)
	keyboard.release(key)

def legion_doom_knight():
	keys = ["2", "3", "4", "5"]
	while True:
		for k in keys:
			sleep(1)
			tap(k)

def vampire_lord():
	keys = {"3" : 2, "2" : 3, "4" : 2, "2" : 3, "2" : 3}
	sleep(2)
	tap("5")
	close_target()
	tap("1")
	for i in range(3):
		for k,v in keys.items():
			tap(k)
			sleep(v)

def vampire_lord_alt():
	keys = ["2", "3", "4"]
	for k in keys:
		tap(k)
		sleep(1)

def lightcaster():
	keys = ["2", "3", "4", "5"]
	for k in keys:
		sleep(1)
		tap(k)
		if k == "4":
			close_target()
			tap("1")

def archpaladin():
	def nought():
		for i in range(4):
			tap("2")
			sleep(5)
		tap("2")
		sleep(1.5)
		tap("3")
		close_target()
		sleep(4)
		tap("2")
		sleep(1.5)
		tap("3")
		close_target()

	nought()
	sleep(5)
	tap("5")

def legion_revenant():
	keys = ["1", "2", "3", "4", "5"]
	for k in keys:
		sleep(1.2)
		tap(k)
		if k == "4":
			close_target()
			tap("1")

def legion_revenant_alt():
	keys = ["2", "3", "5"]
	for k in keys:
		sleep(1.2)
		tap(k)

def darkside():
	keys = ["2", "3", "4", "5"]
	for k in keys:
		sleep(2)
		tap(k)
		if k == "2" or k == "5":
			close_target()
			tap("1")

def lord_of_order():
	keys = ["3", "2", "4", "5"]
	for k in keys:
		tap(k)
		if k in ["3", "2", "4"]:
			close_target()
			tap("1")
		sleep(2)

def doom_kitten():
	while True:
		tap("3")
		sleep(2)

def click_at(x, y, cm=False):
	if cm:
		x = int(x * 1366/34.3)
		y = int(y * 768/19.3)
	mouse.position = (x, y)
	mouse.click(button)
	# sleep(2)

def close_target():
	x = int(15.5 * 1366/34.3)
	y = int((3.4) * 768/19.3)
	click_at(x, y)

def click_screen():
	click_at(14, 16, cm=True)

def click_no():
	x = int(19 * 1366/34.3)
	y = int(4.1 * 768/19.3)
	click_at(x, y)

def accept_drop():
	click_at(637, 600)
	sleep(1)
	click_at(13, 16, cm=True)

def accept_drop2() :
	click_at(15, 12.5, cm=True)

def turn_in():
	# click quest
	click_at(278, 300)
	sleep(1.5)
	# click turn in
	click_at(378, 561)
	sleep(1.5)
	# accept tokens
	click_at(637, 517)
	sleep(1.5)
	# click quest
	click_at(378, 300)
	sleep(1.5)
	# accept quest
	click_at(319, 561)
	sleep(1.5)

def turn_in_bone_dust():
	# click bones dust
	x = int(9 * 1366/34.3)
	y = int(9 * 768/19.3)
	click_at(x, y)
	sleep(1.5)
	# click turn in
	click_at(378, 561)
	sleep(1.5)
	# accept tokens
	click_at(637, 517)
	sleep(1.5)
	# click bones dust
	x = int(9 * 1366/34.3)
	y = int(9 * 768/19.3)
	click_at(x, y)
	sleep(1.5)
	# accept quest
	click_at(319, 561)
	sleep(1.5)

def turn_in_essence():
	# click bones dust
	x = int(9 * 1366/34.3)
	y = int(8.5 * 768/19.3)
	click_at(x, y)
	sleep(1.5)
	# click turn in
	click_at(378, 561)
	sleep(1.5)
	# accept tokens
	click_at(637, 517)
	sleep(1.5)
	# click bones dust
	x = int(9 * 1366/34.3)
	y = int(8.5 * 768/19.3)
	click_at(x, y)
	sleep(1.5)
	# accept quest
	click_at(319, 561)
	sleep(1.5)

def turn_in_necropolis():
	turn_in_bone_dust()
	turn_in_essence()
	

def seraphic_turn_in():
	# Regular medal
	x = int(21 * 1366/34.3)
	y = int(5 * 768/19.3)
	click_at(x, y)
	sleep(1.5)
	# accept tokens
	click_at(637, 517)
	sleep(1.5)
	# Mega medal
	x = int(22 * 1366/34.3)
	y = int(5 * 768/19.3)
	click_at(x, y)
	sleep(1.5)
	# accept tokens
	click_at(637, 517)
	sleep(1.5)

def move_screen():
	x = int(0.5 * 1366)
	y = int((0.5 + 4/19.3) * 768)
	click_at(x, y)
	sleep(2)
	click_at(5, 8, cm=True)
	sleep(6)
	click_at(17, 13, cm=True)

def move_screen2() :
	click_at(28, 12, cm=True)

def return_screen():
	click_at(17, 15.2, cm=True)

def return_screen2() :
	click_at(5, 12, cm=True)

def endless_bridge():
	x = int(29 * 1366/34.3)
	y = int((19.3-10) * 768/19.3)
	while True:
		click_at(x, y)

def fishing():
	x = int(19 * 1366/34.3)
	y = int(13.5 * 768/19.3)
	click_at(x, y)
	sleep(5)

def legion_tokens():
	sleep(3)
	start = time.time()
	end = time.time()
	while True:
		start = time.time()
		while end-start < 200:
			# click_no()
			click_screen()
			legion_revenant_alt()
			end = time.time()
		return_screen()
		accept_drop()
		move_screen()
		print("Turning in at {0}.".format(dt.now()))
		for i in range(3):
			turn_in()
		sleep(3)
		return_screen()

def seraphic_war():
	sleep(3)
	start = time.time()
	end = time.time()
	while True:
		start = time.time()
		while end-start < 180:
			click_no()
			vampire_lord()
			end = time.time()
		sleep(5)
		print("Turning in at {0}.".format(dt.now()))
		for i in range(5):
			seraphic_turn_in()
		sleep(3)

def merge():
	x = int(0.5 * 1366)
	y = y = int(0.75 * 768)
	click_at(x, y)
	sleep(1)

def turn_in_number(x) :
	# click quest
	click_at(378, 260+(x*16))
	sleep(1.5)
	# click turn in
	click_at(378, 561)
	sleep(1.5)
	# accept tokens
	click_at(637, 517)
	sleep(1.5)
	# click quest
	click_at(378, 260+(x*16))
	sleep(1.5)
	# accept quest
	click_at(319, 561)
	sleep(1.5)

def tainted_gem() :
	while True:
		turn_in_number(7)

def nulgath_emblem() :
	sleep(3)
	start = time.time()
	end = time.time()
	while True:
		start = time.time()
		while end-start < 150:
			# click_no()
			click_screen()
			legion_revenant()
			accept_drop()
			accept_drop2()
			end = time.time()
		move_screen2()
		sleep(4)
		print("Turning in at {0}.".format(dt.now()))
		turn_in_number(5)
		sleep(3)
		return_screen2()

def help():
	funcs = {
				"buy" : "merge items",
				"d" : "darkside", 
				"h" : "help",
				"ldk" : "legion doomknight", 
				"loo" : "lord of order",
				"lr" : "legion revenant",
				"lt" : "legion tokens (fotia)", 
				"lc" : "lightcaster", 
				"orb" : "turn in necropolis",
				"sera" : "seraphic turn in",
				"vl" : "vampire lord",
				"vla" : "vampire lord (without 'aspect of the bat'"
			}
	print("Acceptable options:")
	for k,v in funcs.items():
		print("-{0}	:	{1}".format(k,v))
	print("If you would like to accept drops, add '-a'.")

if __name__ == '__main__':
	func = False
	args = len(argv) - 1
	var = argv[1][1::]
	accept = False
	if args == 2 and argv[2][1::] == "a":
		accept = True

	keyboard = Keyboard()
	mouse = Mouse()
	button = Button.left

	if var == "buy":
		func = merge
	elif var == "d":
		func = darkside
	elif var == "h":
		help()
	elif var == "ldk":
		func = legion_doom_knight
	elif var == "loo":
		func = lord_of_order
	elif var == "lr":
		func = legion_revenant
	elif var == "lra":
		func = legion_revenant_alt
	elif var == "lt":
		func = legion_tokens
	elif var == "lc":
		func = lightcaster
	elif var == "orb":
		func = turn_in_necropolis
	elif var == "sera":
		func = seraphic_war
	elif var == "vl":
		func = vampire_lord
	elif var == "vla":
		func = vampire_lord_alt
	elif var == "nem" :
		func = nulgath_emblem
        elif var == "tg" :
            func = tainted_gem
	elif var == "test":
		sleep(2)
		# Put test code here
		accept_drop()
		# click_at(13, 16, cm=True)
		print("Test complete.")
	else:
		print("var passed does not match options")
		help()

	if func != False:
		print("Running from: {0}".format(dt.now()))
		if accept:
			print("Accepting drops.")
		print("Running {0}.".format(func))
		while True:
			try:
				func()
				if accept:
					accept_drop()
			except KeyboardInterrupt as e:
				print("\nSimon ended at {0}".format(dt.now()))
				break
