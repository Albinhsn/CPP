import math
from itertools import combinations
n = int(input())
A = list(map(int, input().split()))
A.sort()
sm = sum(A)
best = max(A[-1], sm-A[-1]) - min(A[-1], sm-A[-1])
for i in range(2,n//2+1):
    comb = combinations(A, i)
    for j in comb:
        j = list(j)
        if best>abs(sm - sum(j)*2):
            best = abs(sm - sum(j)*2)
print(best)