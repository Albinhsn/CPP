for _ in range(int(input())):
    s = input()
    s1 = list(map(int, s[0:3]))
    s2 = list(map(int, s[3::]))
    if sum(s1) == sum(s2):
        print("YES")
    else:
        print("NO")
    