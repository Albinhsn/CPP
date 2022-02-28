from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cnt = Counter()
sm = 0
best = 0
#look for longest distance between 3 (or 2) elements of same kind

