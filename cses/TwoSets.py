n = int(input())

if (n - 3 )% 4 != 0 and n % 4 != 0:
    print("NO")
else:
    print("YES")
    if (n - 3 )% 4 == 0:
        first = [1,2]
        second = [3]
        i = 3
    else:
        first = []
        second = []
        i = 0
    while i<n:
        first.append(i+1)
        first.append(i+4)

        second.append(i+3)
        second.append(i+2)
        i += 4
    print(len(first))
    print(*first)
    print(len(second))
    print(*second)