N = 7
G = [[False for i in range(N)]for j in range(N)]

def solve(y, x, i, m):
    print(i)
    if i == 48:
        print(k)
        return True
    if G[6][0]:
        return False
    if (m == 'L' and (x == 0 or G[y][x-1] == True) and y > 0 and y < 6 and G[y-1][x] == False and G[y+1][x] == False):
        return 0
    if (m == 'R' and (x == 6 or G[y][x+1] == True) and y > 0 and y < 6 and G[y-1][x] == False and G[y+1][x] == False):
        return 0
    if (m == 'U' and (y == 0 or G[y-1][x] == True) and x > 0 and x < 6 and G[y][x-1] == False and G[y][x+1] == False):
        return 0
    if (m == 'D' and (y == 6 or G[y+1][x] == True) and x > 0 and x < 6 and G[y][x-1] == False and G[y][x+1] == False):
        return 0

    if s[i] == "?":
        k = 0
        RR = [1,0,-1,0]
        CC = [0,1,0,-1]
        for j in range(4):
            xx = x + RR[j]
            yy = y + CC[j]
            if yy < 0 or yy > 6:
                continue
            if xx < 0 or xx > 6:
                continue
            if G[yy][xx] == True:
                continue
            G[yy][xx] = True
            k += solve(yy, xx, i+1, 'ULDR'[j])
            G[yy][xx] = False
        return k
    if s[i] == "L":
        x -= 1
    elif s[i] == 'R':
        x += 1
    elif s[i] == 'U':
        y -= 1
    elif s[i] == 'D':
        y += 1
    if x < 0 or x > 6:
        return 0
    if y < 0 or y > 6:
        return 0
    if G[y][x] == True:
        return 0

    G[y][x] = True
    k = solve(y,x,i+1,s[i])
    G[y][x] = False
    return k


s = input()
G[0][0] = True
print(solve(0,0,0,0))
