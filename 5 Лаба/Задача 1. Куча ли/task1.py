import time, tracemalloc

def check(n, a):
	for i in range(1, n + 1):
		if 2 * i <= n:
			if a[i] > a[2 * i]:
				return False
		if 2 * i + 1 <= n:
			if a[i] > a[2 * i + 1]:
				return False
	return True

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
a = list(map(int, f1.readline().split()))
a.insert(0, 0)
if not check(n, a):
	f2.write("NO")
else:
	f2.write("YES")
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
