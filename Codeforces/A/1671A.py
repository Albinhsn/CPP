for _ in range(int(input())):
    s = input()
    if len(s) == 1:
        print("NO")
        continue
    flag = False
    for idx, val in enumerate(s):
        if(idx != 0 and idx != len(s)-1):
            if val != s[idx+1] and val != s[idx-1]:
                flag = True
                print("NO")
                break
        else:
            if idx == 0:
                if s[idx+1] != val:
                    flag = True
                    print("NO")
                    break
            else:
                if s[idx-1] != val:
                    flag = True
                    print("NO")
                    break
                
    if flag == False:
        print("YES")