scanners = []
f = open('input.txt', 'r')
for line in f:
    if '---' in line:
        scanner = {'beacons': []}
        continue
    if line[0] == "\n":
        scanners.append(scanner)
        continue
    beacon =  {'x':0, 'y':0, 'z': 0}
    beacon['x'], beacon['y'], beacon['z']  = line.strip().split(',')
    scanner['beacons'].append(beacon)
scanners.append(scanner)
for i in scanners:
    print(i)


final_cnt = 0

def attempt_point(old_sensor, new_sensor):
    #--- scanner 0 ---
    # 0,2,0
    # 4,1,0
    # 3,3,0

    # --- scanner 1 ---
    # -1,-1,0
    # -5,0,0
    # -2,1,0
    
    for i in range(6):
        pass

#Put a point on top of another and change the others, 
#Check how many overlaps, 
# if more then 13 then "add it after"
    cnt = 0


def recurv_test(old_idx, new_idx):
    pass
# Repeat
# If you can't find on that overlaps after list is done, backtrack and try again



    
    