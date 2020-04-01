from dotpyo import click_at, tap
from time import sleep

class AttackPattern():
	"""
	Takes a list argument, where each element is (int:key, int:wait).
	int:key is the key to be pressed next in the sequence
	int:wait is the time to wait between keys
	For skills that are applied to self, follow with (0, 0), to close the
	target.
	"""
	pattern = []

	def __init__(self, pattern):
		self.pattern = pattern

	def attack(self):
		for p in self.pattern:
			print(p[0], p[1])
			tap(str(p[0]))
			if (p[0] == 0):
				self.close_target()
			sleep(p[1])

	def close_target(self):
		x = int(15.5 * 1366/34.3)
		y = int((3.4) * 768/19.3)
		click_at(x, y)