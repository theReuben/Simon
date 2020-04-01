from libs.attack_pattern import AttackPattern
from libs.functions import accept_drop, turn_in

from datetime import datetime as dt
from time import sleep
from sys import argv

def tainted_gems():
	while True:
		turn_in(num=7)

if __name__ == '__main__':
	var = argv[1]
	func = False

	if var == "tg":
		func = tainted_gems
	elif var == "test" :
		sleep(3)
		# Your code here
		print("Test complete.")

	if func != False:
		print("Running from: {0}".format(dt.now()))
		print("Running {0}".format(func))
		if accept:
			print("Acceptig drops.")

		while True:
			try:
				func.attack()
				if accept:
					accept_drop()
			except KeyboardInterrupt as e:
				print("\nSimon ended at {0}".format(dt.now()))
				break