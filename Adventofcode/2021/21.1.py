from sympy import N


f = open("input.txt", 'r')
p1_pos = int(f.readline().strip().split()[-1])
p2_pos = int(f.readline().strip().split()[-1])
f.close()


rolls = 0
p1 = 0
p2 = 0
cnt = 1
def calc_new_pos(cnt, p_pos):
    n = cnt*3 + 3
    p_pos += n
    if p_pos>10:
        if p_pos % 10 == 0:
            return 10
        p_pos %= 10
    return p_pos    
    
while True:
    new_pos = calc_new_pos(cnt, p1_pos)
    p1 += new_pos
    p1_pos = new_pos
    cnt += 3
    rolls += 3
    if p1>=1000:
        break
    new_pos = calc_new_pos(cnt, p2_pos)
    p2 += new_pos
    p2_pos = new_pos
    cnt += 3
    rolls +=3
    if p2>= 1000:
        break
print(min(p1, p2) * rolls)