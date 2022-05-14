for _ in range(int(input())):
    n = int(input())
    if n %2 != 0 or n<4:
        print(-1)
        continue
    
    MIN = 0
    MAX = n // 4
    if(n % 6 == 0):
        MIN = n // 6
    elif (n == 4):
        MIN = 1
    else:
        MIN = n // 6 + 1
    
    print(MIN, MAX)