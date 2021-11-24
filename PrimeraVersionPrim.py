def prim(G):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n
  aux = [(0, 0)]
  while aux:
    _, z = hq.heappop(aux)
    if not visited[z]:
      visited[z] = True
      for x, y in G[z]:
        if not visited[x] and y < cost[x]:
          cost[x] = y
          path[x] = z
          hq.heappush(aux, (y, x))

  return path, cost
