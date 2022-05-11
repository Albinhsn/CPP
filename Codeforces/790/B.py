for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if len(set(A)) == 1:
        print(0)
        continue
    cnt = 0
    A = sorted(A)
    first = A[0]
    for i in range(1,n):
        cnt += (A[i] - first)
    print(cnt)
    
    