for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    m = input()
    B = list(map(int, input().split()))
    sm = sum(B)
    idx = sm % n
    print(A[idx])