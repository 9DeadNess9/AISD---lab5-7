import random

f1 = open("input.txt", "w")
k, n = map(int, input().split())
f1.write(str(k) + " " + str(n) + "\n")
for i in range(n):
	f1.write(str(random.randint(1, 1000)) + " ")
