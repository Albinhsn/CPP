


for _ in range(int(input())):
    A = input()
    print(A)
    if len(A) == 1:
        print(1)
        print("GOT")
        continue
    flag = False
    
    if "0" not in A:
        for idx, val in enumerate(A):
            if val == "1":
                print(idx+1)
                flag = True
                break
    if not flag:
        for idx, val in enumerate(A):
            if val == 0:
                sm = 0
                for i in range(idx):
                    if A[idx-i] == 1:
                        flag = True
                        print(sm + 1)
                        break                    
                    if A[idx-i] == 0:
                        flag = True
                        print(sm)
                        break        
                    sm += 1
        if not flag:
            print(sm+1)
            flag = True
    if not flag:
        print(len(A))
        