f = open("input.txt", 'r')
p1_pos = int(f.readline().strip().split()[-1])
p2_pos = int(f.readline().strip().split()[-1])
f.close()
def calc_new_pos(p_pos):
    p_pos = [p_pos+1, p_pos+2, p_pos+3]
    p_pos = [i%10 if i>10 else i for i in p_pos]
    return p_pos    
def game(p1, p2, p1_pos, p2_pos, turn):
    global p1_wins
    global p2_wins
    
    if turn == True:
        A = calc_new_pos(p1_pos)
        for i in A:    
            if p1+i<21:
                game(p1+i, p2, i, p2_pos, False)
            else:
                p1_wins +=1 
        return
    else:
        A = calc_new_pos(p2_pos)
        for i in A:
            if p2+i<21:            
                game(p1, p2+i, p1_pos, i, True)
            else:
                p2_wins +=1
        return
p1_wins = 0
p2_wins = 0
game(0, 0, p1_pos, p2_pos, True)
print(p1_wins, p2_wins)
print(max(p1_wins, p2_wins))