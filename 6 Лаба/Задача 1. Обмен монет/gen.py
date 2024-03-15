import random

f1 = open("input.txt", "w")
a = ["A", "D", "?"]
n = int(input())
f1.write(str(n) + "\n")
for i in range(n):
	f1.write(a[random.randint(0, 2)] + " " + str(random.randint(1, 1000000000000000000)) + "\n")
