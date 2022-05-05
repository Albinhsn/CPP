for _ in range(int(input())):
    s = input().strip()
    if s[len(s)//2+1] == input().strip():
        print("YES")
        continue
    print("NO")