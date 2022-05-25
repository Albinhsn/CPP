for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    X = -1
    for i in A:        
        if A[i] != i:
            if X == -1:
                X = i
            else: 
                X = i & X
    print(X)
        