s = input()
cnt = 0
bst = 0
tst = ""
for ch in s:
    if ch == tst:
        cnt += 1
    else:
        tst = ch
        cnt = 1
    if bst < cnt:
        bst = cnt
print(bst)