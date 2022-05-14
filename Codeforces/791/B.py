
n, q = map(int, input().split())
A = list(map(int, input().split()))
sm = sum(A)
dct = {}
BIG = -1
for i in range(q):
    Q = list(map(int, input().split()))
    if(Q[0] == 2):
        sm = n * Q[1]
        dct = {}
        BIG = Q[1]
    elif Q[1] in dct:
        if Q[1] > Q[2]:
            sm += dct[Q[1]] - Q[2]                
        else:
            sm += Q[2] - dct[Q[1]]
        dct[Q[1]] = Q[2]
    elif BIG  == -1:
        if A[Q[1]-1] > Q[2]:
            sm -= A[Q[1]-1] - Q[2]
        else:
            sm += Q[2] - A[Q[1]-1]
        A[Q[1]-1] = Q[2]
    else:
        dct[Q[1]] = Q[2]
        if BIG > Q[2]:
            sm -= BIG - Q[2]
        else:
            sm += Q[2] - BIG
    print(sm)
    
