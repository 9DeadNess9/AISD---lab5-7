import time, tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
d = set()
for i in range(n):
	com, x = f1.readline().split()
	if com == "A":
		d.add(x)
	elif com == "D":
		if x in d:
			d.remove(x)
	else:
		if x in d:
			f2.write("Y" + "\n")
		else:
			f2.write("N" + "\n")
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
