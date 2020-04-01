from libs.functions import merge

from datetime import datetime as dt
from time import sleep
from tqdm import tqdm
from sys import argv

if __name__ == '__main__':
	num = 0
	if len(argv) == 2 :
		num = int(argv[1])

	print("Running from: {0}".format(dt.now()))

	if num > 0:
		for i in tqdm(range(num)):
			merge()
		print("Successfully merged {0} items".format(num))

	else :
		while True :
			merge()