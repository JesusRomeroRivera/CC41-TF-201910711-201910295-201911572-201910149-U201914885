def bfs(G,s):  
    P,Q={s:None},col.deque([s])  
    while Q:  
        u=Q.popleft()  
        for v in G[u]:  
            if v in P:continue  
            P[v]=u  
            Q.append(v)  
    return P 

def bfs_grupo(grupo, plt=None, ciudad = 60):
  nodelist = grupo["puntosEntrega"]
  nodelist.append(grupo["almacen"])
  label = list()
  for nodo in nodelist:
    label.append(str(get_grupo(nodo, ciudad)))
  grafo = [[] for _ in range(len(nodelist))]
  for i, _ in enumerate(nodelist):
    for j, _ in enumerate(nodelist):
      if i == j: continue
      grafo[i].append((j, manhattan_distance(nodelist[i], nodelist[j])))
  path = bfs(grafo, len(nodelist) - 1)
  if(plt == None): return MostrarGrupo(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      a = coordenadas(int(label[i]), ciudad)
      b = coordenadas(int(label[path[i]]), ciudad)
      plt.plot([a[0], b[0]], [a[1], b[1]])