import time, tracemalloc

class fastHash:
    def __init__(self):
        self.table = set()

    def addNumber(self, X, A, B, Ac, Bc, Ad, Bd):
        if X in self.table:
            A = (B + Ac) % 1000
            B = (B + Bc) % 10**15
        else:
            self.table.add(X)
            A = (A + Ad) % 1000
            B = (B + Bd) % 10**15

        X = (X * A + B) % 10**15
        return X, A, B

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
N, X, A, B = map(int, f1.readline().split())
Ac, Bc, Ad, Bd = map(int, f1.readline().split())
table = fastHash()
for i in range(N):
	X, A, B = table.addNumber(X, A, B, Ac, Bc, Ad, Bd)
f2.write(str(X) + " " + str(A) + " " + str(B))
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
