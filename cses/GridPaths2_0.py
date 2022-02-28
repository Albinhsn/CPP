N = 6
G = [[False for i in range(N)] for j in range(N)]
G[0][0] = True
XX = [1,0,-1,0]
YY = [0,1,0,-1]
cnt = 1
paths = 0
dct = {}
P = [(0,0)]
s = input()
for idx,ch in enumerate(s):
    if ch != '?':
        dct[idx+1] = ch
def solve(row,col):
    global cnt
    if cnt >= N**2 and (row,col) == (0, N-1):
        global paths        
        paths += 1
        print(paths)
        return True

    for i in range(4):
        x = XX[i]
        y = YY[i]
        new_node = row + x, col + y
        #Check if out of bounds
        # global inv_pos
        # b = time.time()
        if N<=new_node[0] or new_node[0]<0 or N<=new_node[1] or new_node[1]<0:
            #print("GOT 1")
            # inv_pos += (time.time() -b)
            continue
        # inv_pos += (time.time() -b)

        #Check if already True
        # global visited
        # b = time.time()
        if G[new_node[0]][new_node[1]]:
            # visited += (time.time() - b)
            continue
        # visited += (time.time() - b)
        #Check "Xtra step"
        # global xtra 
        # b = time.time()
        xtra_step = new_node[0] + x, new_node[1] + y
        if xtra_step[0]>=N or xtra_step[0]<0 or xtra_step[1]>=N or xtra_step[1]<0:
            #Check "left" and "right" of first step to check if both are true and then continue
            L = new_node[0] +y, new_node[1] + x
            R = new_node[0] + y * -1, new_node[1] + x * -1
            if L[0]<N and L[0]>0 and L[1]<N and L[1]>0 and R[0]<N and R[0]>0 and R[1]<N and R[1]>0:
                if not G[L[0]][L[1]] and not G[R[0]][R[1]]:
                    # xtra += (time.time() - b)
                    continue

        
        elif G[xtra_step[0]][xtra_step[1]]:
            #Check "left" and "right" of first step to check if both are true
            L = new_node[0] +y, new_node[1] + x
            R = new_node[0] + y * -1, new_node[1] + x * -1
            if L[0]<N and L[0]>0 and L[1]<N and L[1]>0 and R[0]<N and R[0]>0 and R[1]<N and R[1]>0:
                if not G[L[0]][L[1]] and not G[R[0]][R[1]]:
                    # xtra += (time.time() - b)
                    continue
        # xtra += (time.time() - b)
        #Check if in dct
        # global in_str
        # b = time.time()
        if cnt in dct:
            if (x,y) == (1,0):
                if dct[cnt] != 'R':
                    # in_str += (time.time() -b)
                    continue
            elif (x,y) == (-1,0):
                if dct[cnt] != 'L':
                    # in_str += (time.time() -b)
                    continue
            elif (x,y) == (0,1):
                if dct[cnt] != 'D':
                    # in_str += (time.time() -b)
                    continue
            elif (x,y) == (0,-1):
                if dct[cnt] != 'U':
                    # in_str += (time.time() -b)
                    continue
        # in_str += (time.time() -b)
        
        
        #Check if end but not end 
        # global inv_goal
        # b = time.time()
        if new_node == (0, N-1) and cnt <N**2-1:
            # inv_goal += (time.time() -b)
            continue
        # inv_goal += (time.time()- b)
        G[new_node[0]][new_node[1]] = True
        # P.append(new_node)
        cnt += 1
        # global solve_calls
        # solve_calls += 1
        solve(new_node[0], new_node[1])
        G[new_node[0]][new_node[1]] = False
        # P.pop(-1)
        cnt -= 1
    return False
import time
# in_str = 0
# inv_goal = 0
# xtra = 0
# visited = 0
# inv_pos = 0
# solve_calls = 0

a = time.time()
solve(0,0)
# print(f"Solve calls - {solve_calls}")
# print(f"Invalid position - {inv_pos}")
# print(f"In str - {in_str}")
# print(f"Invalid goal - {inv_goal}")
# print(f"Xtra step - {xtra}")
# print(f"Visited - {visited}")
print("tot - ",time.time() - a)
print(paths)