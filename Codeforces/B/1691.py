for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    flag = False
    prev = A[0]
    result = []
    cnt = 1
    for idx in range(1,n):        
        if A[idx] != prev and cnt == 1:            
            flag = True
            break
        if A[idx] != prev:
            result.append(idx)
            for j in range(idx-cnt+1, idx):
                result.append(j)
            cnt = 1            
            prev = A[idx]
            continue
        cnt += 1
        
    
    if flag or n == 1 or cnt == 1:
        print(-1)
        continue
    result.append(n)
    for j in range(n-cnt+1, n-1+1):
        result.append(j)
    print(*result)
         