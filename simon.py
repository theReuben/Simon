from dotpyo import click_at, tap
from time import sleep

class Attack_Pattern():
	"""
	Takes a pattern dict() of the form {(str) k: (int) v} where k is the key,
	and v is the time to wait after pressing in seconds.
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