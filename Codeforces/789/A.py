for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    if 0 in A:
        cnt = 0
        for i in A:
            if i == 0:
                cnt += 1
        print(len(A) - cnt)
        continue
    if len(set(A)) == len(A) and 0 not in A:
        print(len(A) + 1)
        continue
    print(len(A))
