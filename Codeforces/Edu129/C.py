
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A2 = sorted(A)
    B = list(map(int, input().split()))
    B2 = sorted(B)
    if A == sorted(A) and B == sorted(B):
        print(0)
        continue
    flag = False
    
    for i in range(n):        
        if A2.index(A[i]) != B2.index(B[i]) and A2[B2.index(B[i])] != A2[A2.index(A[i])] and B2[B2.index(B[i])] != B2[A2.index(A[i])]:
            flag = True
            break
    if flag:
        print(-1)
        continue
    arr = []
    for i in range(n):                
        if A.index(A2[i]) != i and B[i] <= B2[A.index(A2[i])]:        
            arr.append((A.index(A2[i])+1 ,i+1))
            temp = A[i]
            temp2 = B[i]
            idx = A.index(A2[i])
            A[i] = A[idx]
            A[idx] = temp
            B[i]  = B[idx]
            B[idx] = temp2
            if A == A2 and B == B2:
                break      
    print(len(arr))
    for i in arr:
        print(i[0], i[1])
       