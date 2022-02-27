from itertools import permutations
A = [i for i in input().strip()]
perm = permutations(A)
cnt = 0
s = set()
for i in perm:
    i = "".join(i)
    s.add(i)

print(len(s))
s = list(s)
s.sort()
for i in s:
    print(i)