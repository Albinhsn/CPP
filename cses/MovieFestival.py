import time
a = time.time()
movies = set()
for _ in range(int(input())):
    a,b = map(int, input().split())
    movies.add((a,b))
movies = list(movies)
cnt = 0 
T = 0
while len(movies)>0:
    movies.sort(key=lambda x:x[1])
    cnt += 1
    T = movies[0][1]
    movies.pop(0)
    movies = [i for i in movies if i[0]>=T]
print(cnt)
print(time.time() - a)
#Find movie with lowest end time from start
#Then find next movie with lowest end time starting from prev end time
