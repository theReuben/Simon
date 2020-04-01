from dotpyo import click_at, tap

from time import sleep

def accept_drop():
	click_at(637, 600)
	sleep(1)
	click_at(13, 16, cm=True)

def merge():
	x = int(0.5 * 1366)
	y = int(0.75 * 768)
	click_at(x, y)
	sleep(1)

def turn_in(x = 1) :
	# click quest
	click_at(378, 260+(x*16))
	sleep(1.5)
	# click turn in
	click_at(378, 561)
	sleep(1.5)
	# accept drop
	click_at(637, 517)
	sleep(1.5)
	# click quest
	click_at(378, 260+(x*16))
	sleep(1.5)
	# accept quest
	click_at(319, 561)
	sleep(1.5)