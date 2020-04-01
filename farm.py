from libs.attack_pattern import AttackPattern
from libs.functions import accept_drop

from datetime import datetime as dt
from time import sleep
from sys import argv

def new_lr():
	return AttackPattern([(2,1.5), (3,1.5), (4,1.5), (0,0),	(5,1.5)])


if __name__ == '__main__':
	lr = new_lr()

	accept = False
	func = False
	args = len(argv)
	if args == 2 and argv[1] == "-a":
		accept = True

	if args >= 1:
		func = lr

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