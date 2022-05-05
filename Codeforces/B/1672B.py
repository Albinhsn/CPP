for _ in range(int(input())):
    s = input()
    a = 0
    flag = False;
    if len(s) < 2 or s[0] == "B" or s[-1] != "B":
        print("NO")
        continue
    for ch in s:
        if ch == "A":
            a += 1
        else:
            a -= 1
        if a<0:
            flag = True
            break;
    if flag == False:
        print("YES")
        continue
    print("NO")