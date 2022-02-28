import math
n = int(input())
A = list(map(int, input().split()))
A.sort()
sm = 0
mean = A[math.ceil(len(A)/2)-1]
for i in A:
    sm += (abs(mean - i))
print(sm)