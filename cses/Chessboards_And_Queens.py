
reserv = []
for i in range(8):
    inp = input()
    for idx, val in enumerate(inp):
        if val == '*':
            reserv.append((i, idx))

def isSafe(grid, x, y):
    i = x
    j = y
    #Check left 
    if (y,x) in reserv:
        return False
    while  i>=0:
        i -= 1
        if grid[j][i] == 1:
            return False
        
    
    i = x
    j = y
    #Check above
    while j>=0:
        j -= 1
        if grid[j][i] == 1:
            return False
        


    #Check left diagonal
    i = x
    j = y
    while i>0 and j>0:
        j -= 1
        i -= 1
        if grid[j][i] == 1:
            return False 


    #Check right diagonal
    i = x
    j = y
    while j>0 and i<7:
        j -= 1
        i += 1
        if grid[j][i] == 1:
            return False
    

    return True
        



def solve(grid, y):
    if y == 8:
        global boards
        boards += 1
        return True
    res = False
    for i in range(8):
        if isSafe(grid, i, y):
            grid[y][i] = 1
            res = solve(grid, y+1) or res
            grid[y][i] = 0
    return res

boards = 0
grid = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]]
x, y = 0, 0
solve(grid, 0)
print(boards)
     



