n = int(input())
A = list(map(int, input().split()))
C = [0]
cnt = 1
for i in A:
    if i-1 not in C:
        cnt += 1
    else:
        C.pop(C.index(i-1))
    C.append(i) 
print(cnt)