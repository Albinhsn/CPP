for _ in range(int(input())):
    n = int(input())
    sm = 1
    i = 0
    while sm<n:
        i += 1
        sm += i * 9* 10**(i-1)
    sm -= i * 9* 10**(i-1)
    n -= sm 
    idx = (n) % i
    n = n // i + 10**(i-1)
    n = str(n)
    print(n[idx])