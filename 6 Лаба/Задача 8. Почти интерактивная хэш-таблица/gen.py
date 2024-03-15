import random

f1 = open("input.txt", "w")
f1.write(str(random.randint(1, 10 ** 7)) + " ")
f1.write(str(random.randint(1, 10 ** 15)) + " ")
f1.write(str(random.randint(1, 10 ** 3)) + " ")
f1.write(str(random.randint(1, 10 ** 15)) + "\n")
f1.write(str(random.randint(0, 10 ** 3)) + " ")
f1.write(str(random.randint(0, 10 ** 15)) + " ")
f1.write(str(random.randint(0, 10 ** 3)) + " ")
f1.write(str(random.randint(0, 10 ** 15)) + "\n")
