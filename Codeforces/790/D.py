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
    best = 0
    for i in range(n):
        for j in range(m):
            sm = 0
            cords = {}
            for k in range(4):
                try:
                    Z = 0
                    while True:
                        if j+Z*XX[k] < 0 or i+Z*YY[k] < 0:
                            break
                        if (i+Z*YY[k],j+Z*XX[k]) not in cords:
                            sm += A[i+Z*YY[k]][j+Z*XX[k]]                            
                            cords[(i+Z*YY[k], j+Z*XX[k])] = True
                        
                        Z += 1
                        
                except:
                    pass
            
            if sm > best:
                best = sm
    print(best)
            

        
    