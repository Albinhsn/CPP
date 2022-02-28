import time
a = time.time()
n, m = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))



for i in M:
    j = i
    flag = False
    while j>0:
        if j in N:
            print(j)
            N.pop(N.index(j))
            flag = True
        j -= 1
    if not flag:
        print(-1)
print(time.time() -a)