import random

N = int(input())
print(N)
for i in range(N) :
    print(random.randint(1, 100000), end=' ')
print()
