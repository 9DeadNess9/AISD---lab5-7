import random

f1 = open("input.txt", "w")
n, m, l = map(int, input().split())

f1.write(str(n) + "\n")	
for i in range(n):
	f1.write(str(random.randint(-1000, 1000)) + " ")
f1.write("\n")
f1.write(str(m) + "\n")	
for i in range(m):
	f1.write(str(random.randint(-1000, 1000)) + " ")
f1.write("\n")
f1.write(str(l) + "\n")	
for i in range(l):
	f1.write(str(random.randint(-1000, 1000)) + " ")
