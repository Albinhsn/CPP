import math
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if len(set(A)) >= n // 2:
        print(n // 2)
        continue
    print(math.ceil(len(set(A)) / 2) + 1)
    