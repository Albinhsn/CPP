arr = []
for _ in range(int(input())):
    
    a, n = input().split()
    a = int(a)
    n = int(n)
    alph = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
    }
    A = []
    for i in range(a):
        A2 = input()
        A.append(A2)
    xd = []
    for i in range(0,a-1):
        for j in range(i+1,a):
            dif = 0
            for k in range(0,n):
                dif += abs(alph[A[i][k]]-alph[A[j][k]])
            xd.append(dif)
    print(sorted(xd)[0])          