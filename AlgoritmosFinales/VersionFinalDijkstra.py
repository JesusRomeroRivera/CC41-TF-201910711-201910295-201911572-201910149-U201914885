def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  while queue:
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))
  return path, cost

def dijkstra_grupo(grupo, plt=None, ciudad = 60):
  nodelist = grupo["puntosEntrega"]
  nodelist.append(grupo["almacen"])
  label = list()
  for nodo in nodelist:
    label.append(str(get_grupo(nodo,ciudad)))
  grafo = [[] for _ in range(len(nodelist))]
  for i, _ in enumerate(nodelist):
    for j, _ in enumerate(nodelist):
      if i == j: continue
      grafo[i].append((j, manhattan_distance(nodelist[i], nodelist[j])))
  path, cost = dijkstra(grafo, len(nodelist) - 1)
  if(plt == None): return MostrarGrupo(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      a = coordenadas(int(label[i]), ciudad)
      b = coordenadas(int(label[path[i]]), ciudad)
      plt.plot([a[0], b[0]], [a[1], b[1]])
