def prim(G):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n
  q = [(0, 0)]
  while q:
    _, u = hq.heappop(q)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        if not visited[v] and w < cost[v]:
          cost[v] = w
          path[v] = u
          hq.heappush(q, (w, v))

  return path, cost

def prim_grupo(grupo, plt=None, ciudad = 60):
  nodelist = grupo["puntosEntrega"]
  nodelist.append(grupo["almacen"])
  label = list()
  for nodo in nodelist:
    label.append(str(get_grupo(nodo,ciudad)))
  grafo = [[] for _ in range(len(nodelist))]
  for i, _ in enumerate(nodelist):
    for j, _ in enumerate(nodelist):
      if i == j: 
        continue
      grafo[i].append((j, manhattan_distance(nodelist[i], nodelist[j])))
  path, cost = prim(grafo)
  if(plt == None): return MostrarGrupo(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      a = coordenadas(int(label[i]), ciudad)
      b = coordenadas(int(label[path[i]]), ciudad)
      plt.plot([a[0], b[0]], [a[1], b[1]])
