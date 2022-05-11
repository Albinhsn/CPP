arr = []
for _ in range(int(input())):
    n,q = map(int,input().split())
    A = list(map(int,input().split()))
    
    for i in range(q):
        N = int(input())
        if sum(A) < N:
            print(-1)        
            
            continue
        sm = 0
        cnt = 0
        for j in A:
            sm += j
            cnt += 1
            if sm >= N:
                print(cnt)
                break