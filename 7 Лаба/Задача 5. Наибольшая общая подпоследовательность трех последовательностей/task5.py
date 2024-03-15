import time, tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
A = list(map(int, f1.readline().split()))
m = int(f1.readline())
B = list(map(int, f1.readline().split()))
l = int(f1.readline())
C = list(map(int, f1.readline().split()))
dp = [[[0 for i in range(l+1)] for j in range(m+1)] for k in range(n+1)]  
for i in range(1, n+1):
	for j in range(1, m+1):
		for k in range(1, l+1):
			if A[i-1] == B[j-1] == C[k-1]:
				dp[i][j][k] = dp[i-1][j-1][k-1] + 1
			else:
				dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
f2.write(str(dp[n][m][l]))
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
