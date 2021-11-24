#Primer versión implementada del algoritmo BFS
def bfs(G, pos):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  visited[pos] = True  
  q = [pos]

  while queue:
    a = q.pop(0)
    for i in G[a]:
      if not visited[i]:
        visited[i] = True
        parent[i] = a
        q.append(i)

  return parent
