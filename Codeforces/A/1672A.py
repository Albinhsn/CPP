import math
for _ in range(int(input())):
    l = input()
    x = input().split()
    SUM = 0
    for i in x:
        SUM += int(i) - 1  
    if SUM % 2 != 0:
        print("errorgorn")
        continue
    print("maomao90")
     