import numpy as np 
def isSafe(board, row, col):
 
    # Check this row on left side
    for i in range(col):
        if (board[row][i]):
            return False
 
    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return False
        i -= 1
        j -= 1
 
    # Check lower diagonal on left side
    i = row
    j = col
    while j >= 0 and i < 4:
        if(board[i][j]):
            return False
        i = i + 1
        j = j - 1
 
    return True
    
        



import time
def move(x,y):
    if x<3:
        x+=1
    else:
        x =0
        y += 1
    return x,y

boards = 0
def solve(grid, y, boards):
    print(grid, y)
    time.sleep(1)
    if y == 4:
        boards += 1
        return True
    res = False
    for i in range(4):
        if isSafe(grid, i, y):
            grid[i][y] = 1
            res = solve(grid, y+1, boards) or res
            grid[i][y] == 0
    return res

grid = [[0 for j in range(4)]
            for i in range(4)]
x, y = 0, 0    
        
    
print(solve(grid,y, boards))
print(grid)
