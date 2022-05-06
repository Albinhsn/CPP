for _ in range(int(input())):
    n, m = input().split()
    A = list(map(int, input().split()))
    if int(n)>int(m):
        print("NO")
        continue
    
    A = sorted(A, reverse=True)
    sm = A[0] * 2 + sum(A[1:-1]) + int(n)
    if sm > int(m):
        print("NO")
    else:
        print("YES")