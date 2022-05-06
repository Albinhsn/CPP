for _ in range(int(input())):
    a,b,c,x,y = map(int, input().split())
    left = 0
    if y-b>0:
        left += y-b
    if x-a>0:
        left += x-a 

    if(left-c>0):
        print("NO")
        continue
    print("YES")