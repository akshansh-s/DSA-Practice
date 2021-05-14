adj =  [[0, 40, 0, 50, 0, 0],
        [0, 0, 30, 0, 0, 0],
        [0, 0, 0, 0, 20, 50],
        [0, 0, 10, 0, 40, 0],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0]]
 
# we can also show no edge by -1
 
v = len(adj)
inf = 999999999999999999
dist = [inf]*v
dist[0] = 0
visited = [False]*v


for i in range(v):
    mindist = inf
    x = -1
 
    for j in range(v):
        if not visited[j] and dist[j] < mindist:
            x = j
            mindist = dist[j]
 
    visited[x] = True
 
    for j in range(v):
        if not visited[j] and adj[x][j] > 0:
            dist[j] = min(dist[j], dist[x] + adj[x][j])
 
print(dist)
 
