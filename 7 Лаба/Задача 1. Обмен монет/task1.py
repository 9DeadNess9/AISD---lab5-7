import time, tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
money, k = map(int, f1.readline().split())
a = list(map(int, f1.readline().split()))
dp = [100000] * (money + 1)
dp[0] = 0
for x in a:
	for i in range(x, money + 1):
		if dp[i] != 100000:
			dp[i] = min(dp[i], dp[i - x] + 1)
		else:
			dp[i] = dp[i - x] + 1
if dp[money] >= 100000:
	f2.write(str(-1))
else:
	f2.write(str(dp[money]))
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
