n,m, k = map(int, input().strip().split())
N = list(map(int, input().strip().split()))
M = list(map(int, input().strip().split()))
N.sort()
M.sort()
i = 0
j = 0
cnt = 0
while len(N)>i and len(M)>j:
    if abs(N[i]-M[j])<=k:
        cnt += 1
        i += 1   
        j +=1
    #If house price is higher then applicant
    elif N[i]<M[j]:
        i += 1
    elif N[i]>M[j]:
        j += 1

print(cnt)