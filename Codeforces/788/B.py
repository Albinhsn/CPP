
arr = []
for _ in range(int(input())):
    input()
    s = [i for i in input()]
    A = input().split()
    A.pop(0)
    sm = 0
    while True:
        toPop = []
        found = False
        popped = 0
        for idx, i in enumerate(s[:]):
            if i in A and idx != 0:
                s.pop(idx-1-popped)
                popped += 1
                found = True
        if not found:
            break
        sm += 1
    arr.append(sm)
print(arr)