n = int(input())
odd = [i for i in range(1,n+1) if i%2 != 0]
even = [i for i in range(1,n+1) if i%2 == 0]
if len(even) == 0:
    print(*odd)
elif len(odd + even)<=3:
  print("NO SOLUTION")    
elif odd[-1] - 1 != even[0] and odd[-1] + 1 != even[0]:
    ans = odd + even
    print(*ans)
else:
    ans = even + odd
    print(*ans)