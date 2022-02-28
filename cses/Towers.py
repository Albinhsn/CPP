import bisect
n = int(input())
A = list(map(int, input().split()))

C = []
for i in A:
    idx = bisect.bisect_right(C,i)
    if idx == len(C):
        C.append(i)
    elif len(C) == 0:
        C.append(i)
    else:
        C[idx] = i
print(len(C))