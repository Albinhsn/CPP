from collections import Counter
cnt = Counter()
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x,y+1):
        cnt[i] += 1
print(cnt.most_common(1)[0][1])