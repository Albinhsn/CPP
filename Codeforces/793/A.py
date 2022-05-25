import math
for _ in range(int(input())):
    n = int(input())
    s = input()    
    cnt = 0
    
    
    middle = math.ceil(n//2)
    
    for i in range(middle, n):
        
        if s[middle] == s[i]:
            cnt += 2
        else:
            break
        
        if middle+i == n-2:
            break
    if n % 2 != 0:
        cnt -= 1
    print(cnt)