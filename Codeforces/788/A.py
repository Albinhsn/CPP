for _ in range(int(input())):
    n = input()
    A = list(map(int, input().split()))
    if sorted(A) == A:
        print("YES")
        continue
    
    sm = 0
    for i in A:
        if i<0:
            sm += 1
    neg = A[0:sm]
    pos = A[sm::]
    for idx, val in enumerate(neg):
        if val>0:
            neg[idx] *= -1
    for idx, val in enumerate(pos):
        if val<0:
            pos[idx] *= -1
    
    if sorted(neg) == neg and sorted(pos) == pos:
        print("YES")
    else:
        print("NO")