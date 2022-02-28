import bisect

n, m = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))
N.sort()
for i in M:
    A = [j for j in N if i-j>=0]
    if len(A)>0:
        print(max(A))
        N.pop(N.index(max(A)))
    else:
        print(-1)
    

