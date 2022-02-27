input()
A = list(map(int, input().split()))
cnt = 0
prev = 0
for i in A:
    if i<prev:
        cnt += prev -i
    else:
        prev = i
print(cnt)