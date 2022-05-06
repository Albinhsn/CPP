import math


for _ in range(int(input())):
    input()
    
    A = list(map(int, input().split()))
    if A == sorted(A) and len(set(A)) == len(A):
    
        print("0")
        continue
    # flag = False
    # lowest = [1]
    # for i in A:
    #     if i <= lowest[-1]:
    #         print("-1")
    #         flag = True
    #         break
    #     while i > lowest[-1]:
    #         i = math.floor(i / 2)
        
        
    # if flag:
    #     continue
    sum = 0;
    flag = False
    for i in range(len(A)):
        if i != len(A) - 1:
            while A[-i-1] <= A[-i-2]:
                A[-i-2] = math.floor(A[-i-2] / 2)
                sum += 1
                if A[-i-1] == 0 and i+1 != len(A):
                    print("-1")
                    flag = True
                    break
                    
    if not flag:
        print(sum)