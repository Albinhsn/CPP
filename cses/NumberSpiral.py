for _ in range(int(input())):
    y,x = map(int, input().split())
    ans = 0
    if y == x:
        print(1 + (y-1) * y)
        continue
    ans = max(y,x) ** 2
    if y > x:
        if y % 2 == 0:
            print (ans - (x-1))
            continue
        else:
            print(ans + (x-1) - (y-1) * 2)
            continue
    if x % 2 == 0:
        print(ans + (y-1) - (x-1) * 2)
        continue
    print(ans - (y-1))
    
        

    
