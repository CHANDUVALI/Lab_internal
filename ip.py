import sys
args=sys.argv[1]
with open("ip.txt") as f:
	for line in f:
		
		if args in line:
			print("ip present :",args)
			sys.exit()
