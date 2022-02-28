from collections import Counter
n, x = map(int, input().split())
A = list(map(int, input().split()))
cnt = Counter(A)
flag = False
for idx, val in enumerate(cnt.elements()):
    if x-val in cnt:
        if x-val == val and cnt[val]>1:
            index = [i for i,x in enumerate(A) if x == val]
            print(index[0]+1, index[-1]+1)
            flag = True
            break
        elif x-val != val:
            print(A.index(val)+1, A.index(x-val)+1)
            flag = True
            break

if not flag:
    print("IMPOSSIBLE")