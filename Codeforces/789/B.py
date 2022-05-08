arr = []
for _ in range(int(input())):
    n = int(input())
    s = input()
    ch = ""
    cnt = 0
    odd = False
    op = 0
    
    for i in range(n):
        
        if not odd:
            if s[i] != ch:
                if cnt % 2 != 0:    
                    odd = True
                    op += 1
                    cnt = 1          
                if cnt % 2 == 0:
                    cnt += 1
                ch = s[i]
            else:
                cnt += 1
        else:            
            if s[i] == ch:
                if cnt % 2 != 0:
                    op = op - cnt + 1
                    odd = False
                cnt = 1
            if s[i] != ch:
                op += 1
                cnt += 1
    print(op)