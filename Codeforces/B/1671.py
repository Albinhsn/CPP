for _ in range(int(input())):
    n = input()
    A = list(map(int, input().split()))
    found = False
    flag = False
    added = False
    subtract = False
    trip = False
    for idx, val in enumerate(A):
        if idx != int(n) - 1:    
            
            if val + 3 < A[idx+1] :
                flag = True
                break
            if val + 3 == A[idx +1]:
                if trip:
                    flag = True
                    break
                trip = True
                if added:
                    flag = True
                    break
            if val + 2 == A[idx + 1]:
                if trip: 
                    flag = True
                    break
                if added and subtract: 
                    flag = True
                    break
                if added and not subtract:
                    subtract = True
                if not added:
                    added = True
            
            
    if flag:
        print("NO")
    else:
        print("YES")
