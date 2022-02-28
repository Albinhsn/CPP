N = int(input())
A = list(map(int, input().split()))
i = 1
cnt = 1
while i< len(A)-1:
    if A.index(i)>A.index(i+1):
        cnt += 1    

    i += 1
print(cnt)
