hit = {}
 
n, q = map(int, input().split())
 
for i in range(q):
    print(i, " HIGh")
    Q = list(map(int, input().split()))
 
    if Q[0] == 1:        
        if (1, Q[2]) in hit:
            hit[(1, Q[2])] += 1
        else:
            hit[(1, Q[2])] = 1
        if (0, Q[1]) in hit:
            hit[(0, Q[1])] += 1
        else:
            hit[(0, Q[1])] = 1
        continue
    if Q[0] == 2:                    
        if hit[(1, Q[2])] == 1:
            del hit[(1, Q[2])]
        else:
            hit[(1, Q[2])] -= 1    
        if hit[(0, Q[1])] == 1:
            del hit[(0, Q[1])]
        else:
            hit[(0, Q[1])] -= 1
        continue
    else:
        flag = False
        for i in range(Q[1], Q[3]+1):
            print(i, " LOW")      
            if (0, i) not in hit:                                    
                for j in range(Q[2], Q[4]+1):                
                    if (1, j) not in hit:
                        print("NO")
                        flag = True
                    break
            if flag:
                    break
        if not flag:
            print("YES")