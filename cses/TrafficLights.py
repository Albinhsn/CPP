from bisect import bisect_left
x, n = list(map(int, input().split()))
A = map(int, input().split())
dct = {}
C = [x]
best = 0
for i in A:
    idx = bisect_left(C,i)
    if idx+1<len(C) or idx-1>0:
        if (C[idx],C[idx+1]) in dct:
            del C[C[idx],C[idx+1]]
        if (C[idx-1],C[idx]) in dct:
            del C[C[idx-1],C[idx]]
    C.insert(idx, i)
    if idx>0:
        dct[(idx-1, idx)] = abs(C[idx-1]-C[idx])
    if idx<len(C):
        dct[(idx, idx+1)] = abs(C[idx] - C[idx+1])
    print(dct)
    print(C)
    print(sorted(dct.values())[-1])
    
