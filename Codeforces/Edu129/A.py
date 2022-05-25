for _ in range(int(input())):
    n = int(input())
    A = sorted(list(map(int, input().split())))
    m = int(input())
    B = sorted(list(map(int, input().split())))    
    flag = False

    if A[-1] > B[-1]:
        print("Alice")
        print("Alice")
        flag = True
        
    if B[-1] > A[-1]:
        print("Bob")
        print("Bob")
        flag = True        
        
    if not flag:
        print("Alice")
        print("Bob")
    
        
