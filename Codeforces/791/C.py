hit = {}

n, q = map(int, input().split())
X = [0 for _ in range(n)]
Y = [0 for _ in range(n)]

for i in range(q):
    Q = list(map(int, input().split()))

    if Q[0] == 1:        
        if (1, Q[2]) in hit:
            hit[(1,Q[2])] += 1
        else:
            hit[(1,Q[2])] = 1
            Y[Q[2]-1] = 1
        if (0, Q[1]) in X:
            hit[(0,Q[1])] += 1
        else:
            hit[(0, Q[1])] = 1
            X[Q[1]-1] = 1
        continue
    if Q[0] == 2:                    
        if hit[(1,Q[2])] == 1:
            del hit[(1,Q[2])]
            Y[Q[2]] = 0
        else:
            hit[(1,Q[2])] -= 1
        if hit[(0,Q[1])] == 1:
            del hit[(0,Q[1])]
            X[Q[1]] = 0
        else:
            hit[(0, Q[1])] -= 1
        continue
    else:
        print(X)
        print(Y)
        print(sum(X[Q[1]-1:Q[3]]), X[Q[1]-1:Q[3]])
        print(sum(Y[Q[2]-1:Q[4]]), Y[Q[2]-1:Q[4]])
        if sum(X[Q[1]-1:Q[3]]) == Q[3]-Q[1]:
            print("YES")
            continue
        if sum(Y[Q[2]-1:Q[4]]) == Q[4]-Q[2]:
            print("YES")
            continue
        print("NO")
    
    
        
