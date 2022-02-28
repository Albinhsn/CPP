movies = set()
for _ in range(int(input())):
    a,b = map(int, input().split())
    movies.add((a,b))
movies = list(movies)
movies.sort(key=lambda x:x[1])
cnt = 0 
ET = 0
for start, end in movies:
    if start>= ET:
        ET = end
        cnt += 1
print(cnt)
#Find movie with lowest end time from start
#Then find next movie with lowest end time starting from prev end time
