s = input()
dct = {}
for idx, ch in enumerate(s):
    if ch != '?':
        dct[idx+1] = ch
def safe(grid_path, d):
    L = len(grid_path)
    new_node = (grid_path[-1][0] + d[0], grid_path[-1][1] + d[1])
    if new_node in grid_path:
        return False
    ch = pos_dct[d] 
    if L in dct:
        if dct[L] != ch:
            return False
    xtra_step = new_node[0] + d[0], new_node[1] + d[1]
    x, y = new_node[0] + d[1] * -1,  new_node[1] + d[0] * -1
    x2, y2 = new_node[0] + d[1],  new_node[1] + d[0] 
    if N <= xtra_step[0] or xtra_step[0]<0 or N<= xtra_step[1] or xtra_step[1] < 0 or xtra_step in grid_path:    
        if ((x,y) not in grid_path and ((N > x and x>=0) and (N>y and y>=0))) and ((x2,y2) not in grid_path and ((N >x2 and x2>=0) and (N>y2 and y2>=0))):
            return False
    if N <= new_node[0] or new_node[0]<0 or N <= new_node[1] or new_node[1]<0:
        return False

    if new_node == (0,N-1) and L<N**2-1:
        return False

    return True
import time
def solve(grid_path):
    if len(grid_path) >=N**2 and grid_path[-1] == (0,N-1):    
        global nmbr_of_paths
        nmbr_of_paths += 1
        #print(nmbr_of_paths)
        return True
    res = False
    for i in range(4):
        x = XX[i]
        y = YY[i]

        if safe(grid_path, (x,y)):  
            grid_path.append((grid_path[-1][0] + x, grid_path[-1][1] + y))
            res = solve(grid_path) or res
            grid_path.pop(-1)
    return res
pos_dct = {(1,0): 'R', (-1,0): 'L', (0,1): 'D', (0,-1): 'U'}
grid_path = [(0,0)]
nmbr_of_paths = 0
N = 7
XX = [1,0,-1,0]
YY = [0,1,0,-1]
A = time.time()
solve(grid_path)
print(nmbr_of_paths)
print(time.time() - A)