n = int(input())
A = list(map(int, input().split()))

C = [[0]]
flag = False
for i in A:
    for j in C:
        if j[-1] +1 == i:
            j.append(i)
            flag = True
            break
    if not flag:
        C.append([i])
print(len(C))