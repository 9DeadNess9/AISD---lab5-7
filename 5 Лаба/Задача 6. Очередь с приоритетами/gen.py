import random

f1 = open("input.txt", "w")
n = int(input())
a = []
f1.write(str(n) + "\n")	
for i in range(n):
	x = round(random.uniform(1, 1000000), 2)
	while x in a:
		x = round(random.uniform(1, 1000000), 2)
	a.append(x)
	f1.write(str(x) + " ")
