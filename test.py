from attack_pattern import AttackPattern
from time import sleep

if __name__ == '__main__':
	sleep(3)
	pattern = [	(2,1.5),
				(3,1.5),
				(4,1.5),
				(0,0),
				(5,1.5)
				]

	lr = AttackPattern(pattern)
	lr.attack()