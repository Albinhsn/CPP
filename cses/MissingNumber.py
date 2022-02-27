n = input()

A = list(map(int, input().split()))
T = [i for i in range(1,int(n)+1)]
ans = list(set(T) - set(A))
print(ans[0])