n = int(input())
for i in range(0, 1<<n):
        gray=i^(i>>1)
        s = "{0:0{1}b}".format(gray,n)
        print(s)