arr = []
for _ in range(int(input())):
    n, m = input().split()
    n = int(n)
    m = int(m)
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    XX = [1,-1,1,-1]
    YY = [1,-1,-1,1]
    XXYY = [1,-1]
    best = 0
    cords = {}
    for i in range(n):
        sm = 0
        
        for j in  XXYY:
            
        cords[i] = sm
        
    print(cords)