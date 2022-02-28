n, m = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))
N.sort()
for i in M:
    A =[j for j in N if i-j>=0]
    if len(A)>0:
        print(A[-1])
        N.pop(N.index(A[-1]))
    else:
        print(-1)
