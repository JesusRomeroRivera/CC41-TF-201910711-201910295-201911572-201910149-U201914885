G = nx.read_weighted_edgelist('1.csv', create_using=nx.DiGraph, delimiter=',', nodetype=int)
def UCS(G, s):
  for u in G.nodes:
    G.nodes[u]['visited'] = False
    G.nodes[u]['path']    = -1
    G.nodes[u]['cost']    = math.inf

  G.nodes[s]['cost'] = 0
  q = [(0, s)]
  while q:
    g_u, u = hq.heappop(q)
    if not G.nodes[u]['visited']:
      G.nodes[u]['visited'] = True
      for v in G.neighbors(u):
          if f_v < g_v:
            G.nodes[v]['cost'] = f_v
            G.nodes[v]['path'] = u
            hq.heappush(q, (f_v, v))

  path = [0]*G.number_of_nodes()
  for v, info in G.nodes.data():
    path[v] = info['path']

  return path