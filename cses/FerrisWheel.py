n, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cnt = 0
visited = 0
i = 0
j = -1
while visited<len(A):
    if A[i] + A[j]>x:
        cnt += 1
        visited += 1
        j -= 1
    else:
        cnt += 1
        visited += 2
        i += 1
        j -= 1
print(cnt)

