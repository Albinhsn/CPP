

s = input()
dct = {}
for ch in s:
    if ch in dct:
        dct[ch] += 1
    else:
        dct[ch] = 1

B = ""
M = ""
flag = False
for key, val in dct.items():
    if val % 2 == 0:
        for i in range(val//2):
            B += str(key)
    else:
        if len(s) % 2 == 0:
            print("NO SOLUTION")
            exit()
        elif flag == False:
            for i in range(val):
                M += str(key)
            flag = True 
        else:
            print("NO SOLUTION")
            exit()
print(B+M+B[::-1])