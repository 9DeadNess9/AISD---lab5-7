import time, tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
a = []
mi = -1
m = 999999999
k = 0
for i in range(n):
	s = list(f1.readline().split())
	if len(s) == 1:
		a.append(999999999)
		if k != 0:
			f2.write(str(m) + "\n")
			a[mi] = 999999999
			k -= 1
			if k != 0:
				m = min(a)
				mi = a.index(m)
			else:
				m = 999999999
				mi = -1
		else:
			f2.write("*\n")
	elif len(s) == 2:
		a.append(int(s[-1]))
		if int(s[-1]) < m:
			m = int(s[-1])
			mi = i 
		k += 1
	else:
		a.append(999999999)
		a[int(s[1]) - 1] = int(s[2])
		if int(s[2]) < m:
			m = int(s[2])
			mi = int(s[1]) - 1
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())

