# Problema de Enrutamiento de Vehículos (VRP) 

#### CC41 - TRABAJO FINAL COMPLEJIDAD ALGORÍTMICA 2021

|INTEGRANTES |CÓDIGO |
|-|-|
|Emanuel Josias Ticona Calsín |U201910295 |
|José Sebastián Hernández Morales |U201914885|
|Gabriel Ignacio Vásquez Guerra |U201910149|
|Jesús Daniel Romero Rivera |U201910711|
|Manuel Alonso Aranguri Vargas |U201911572|

## PROBLEMA
El objetivo se basa en descubrir soluciones óptimas para el problema de enrutamiento de vehículos (VRP). Cuya definición hace referencia a un problema de optimización de carácter combinatorio y de programación de entero que busca hallar el conjunto rutas más óptima para una determinada flota de vehículos que debe satisfacer las demandas de un conjunto dado de clientes.

 
 ## MARCO TEÓRICO
 ### Algoritmo BFS (Breadth First Search)
El algoritmo DFS es unAlgoritmo recursivo, Se necesita una pila de trabajo recursiva, por lo que su complejidad espacial es O (| V |). El proceso de atravesar el gráfico es esencialmente el proceso de encontrar sus puntos vecinos para cada vértice. El tiempo que lleva depende de la estructura de almacenamiento utilizada. Cuando se representa mediante una matriz de adyacencia, el tiempo necesario para encontrar el punto adyacente de cada vértice es O (| V |), por lo que la complejidad del tiempo total es O (| V * V |). Cuando se representa mediante una lista de adyacencia, el tiempo requerido para encontrar los puntos vecinos de todos los vértices es O (| E |), y el tiempo requerido para acceder a los vértices es O (| V |). En este momento, la complejidad de tiempo total es O (| V | + | E |)

 
 ### Algoritmo DFS (Depth First Search)
BFS es un algoritmo de desplazamiento en que se empieza a desplazar desde un nodo específico uno por uno explorando todos los nodos vecinos.
En la función iniciar() se corre la función DFS en todos los nodos, ya que el grafo podría tener dos partes diferentes desconectadas.
La función principal de este algoritmo es averiguar si es que un nodo existe en el grafo.
Teóricamente, DFS se utiliza para atravesar un grafo entero, lo que toma un tiempo de O(|V| + |E|) donde |V| es el número de vértices y |E| es el número de bordes.
Si no se marcaran los nodos como visitados, se podría visitar el mismo nodo varias veces lo que podría ocasionar que se llegue a un bucle infinito.

>  *Para este algoritmo en particular, se emplea el backtracking, método esencial para implementar el algoritmo.*
 
 ### Algoritmo de Dijkstra
La cola (de prioridad) toma un tiempo O(V). Primero se agregan los vértices del grafo a la cola, tras estar completada, el ciclo while es ejecutado por cada vértice. Dentro del ciclo while, cada llamada a extraer_minimo toma un tiempo O(logV). En conjunto estas dos partes toman un tiempo O(Vlog(V))
El ciclo for es ejecutado por cada arista, y en cada uno, la funcion adicionar toma un tiempo O(Elog(V)). Luego, el tiempo de ejecución combinado es O((V+E)log(V)). La complejidad computacional, considerando que el algoritmo tiene n-1 iteraciones como maximo por los vertices añadidos, y que en cada iteracion se identifica un vertice (n-1) y se realiza una suma y comparación, en cada iteración se tienen 2(n-1) operaciones. Entonces el algoritmo realiza O(n^2) operaciones

 
 ### Algoritmo de Prim
Elegir un vértice cualquiera => Vértice de partida.
Seleccionar la arista que tenga menor peso adyacente al vértice de partida -> Se selecciona el otro vértice en el que colinda dicha arista.
Repetir el paso anterior si => La arista elegida tenga conexión con un vértice ya seleccionado y otro que no.
El algoritmo finaliza cuando todos los vértices del grafo han sido seleccionados.
 
 > - La implementación del algoritmo de Prim contempla un tiempo de complejidad O(n^2). Sin embargo, en el pseudocodigo propuesto la implementación es a traves de un montículo. Por ello, la complejidad de nuestro algoritmo sería O(log(n)).
 
 ### Algoritmo UCS
 UCS es un algoritmo que se utiliza para recorrer sobre grafos el camino más corto entre 2 nodos: raíz y destino. Asismismo, se encuentra en la categoríad de algoritmos de búszqueda no informada. La búsqueda inicia por el nodo raíz y pasa al siguiente nodo que tiene menor costo total desde la raíz.

Lo que caracteriza a este algoritmo es que a diferencia de BFS, este emplea una cola de prioridad. Donde, el elemento de menor costo se encuentra al frente.

El tiempo para el caso peor y uso de memoria O(b1 + C*/ε), donde C* es el costo de la solución óptima y b es el factor de ramificación. Asimismo, podemos interpretar C*/ε como el número de pasos que le tomaría llegar a la meta, considerando que cada una de esas acciones es de costo mínimo. Cuando todos los costos entre los nodos son iguales, esto se convierte en O(b^d + 1)^2​

En lo que a calidad se refiere, el algoritmo nos retorna la solución óptima. Además presenta la carácterística de ser un algoritmo completo.
 
 ## DESARROLLO
 ### Creación del Grafo 
 Se importa las librerías y la información de los dataset de los puntos de entrega y los almacenes, ambos en archivos **CSV** que se usara para la creación del grafo. Ademas definimos una función para generar las ciudades. 
 
 ```python 
import graphviz as gv
import numpy as np
import pandas as pd
import heapq as hq
import numpy.random as npr
import matplotlib.pyplot as plt
import collections as col
import networkx as nx
import math
import csv

almacenes = pd.read_csv("https://raw.githubusercontent.com/JesusRomeroRivera/cc41-tf-201910711-201910295-201911572-201910149-201914885/main/datasets/almacenes.csv")

puntos_entrega = pd.read_csv("https://raw.githubusercontent.com/JesusRomeroRivera/cc41-tf-201910711-201910295-201911572-201910149-201914885/main/datasets/puntos_entrega.csv")

def generar_ciudad(tamaño):
  G = [[] for _ in range(tamaño**2)]
  final = False
  for i in range(tamaño ** 2):
    if i % tamaño == 0:
      G[i].append(i+1)
    elif (i + 1) % tamaño == 0:
      G[i].append(i-1)
    else:
      G[i].append(i+1)
      G[i].append(i-1)
    if (tamaño - 1)*tamaño == i:
      final = True
    if not final:
      G[i].append(i+tamaño)
      G[i + tamaño].append(i)
  identificador = ["N" for _ in range(tamaño**2)]
  return G, identificador

  #Características para representar el grafo

  G, identificador = generar_ciudad(2800)
almacenes = pd.read_csv("almacenes.csv", header=None).to_numpy()
pEntrega = pd.read_csv("puntos_entrega.csv", header=None).to_numpy()
plt.subplots(figsize=(17, 17))
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.scatter(almacenes[:, 0], almacenes[:, 1], color = "blue")
plt.scatter(pEntrega[:, 0], pEntrega[:, 1], color = "magenta")

 ```
 
  ### Visualización del grafo
 ![Imagen del grafo](https://raw.githubusercontent.com/JesusRomeroRivera/cc41-tf-201910711-201910295-201911572-201910149-201914885/main/GrafoFinal/almacenes_%20y_ptos_%20entrega.jpg)
 

 ### Creación de regiones de distribución de cada almacén
 A partir de este punto de definimos 2 funciones, una para calcular la distancia entre dos puntos de entrega, y otro para obtener el grupo de estas. 
   ```python 
#Distancia
def manhattan_distance(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Grupos
def get_grupo(coord, size):
  return int(coord[0] + size*coord[1])
 ```
De igual forma, definimos funcionalidades para aplicar lo anteriormente estipulado y crear las coordenadas para dichos puntos

```python
pEntrega_por_almacen = len(pEntrega) / len(almacenes)
pEntrega_aux = list(pEntrega)
grupos = []
grupo = dict()
j= (int)(pEntrega_por_almacen)
for almacen in almacenes:
  pEntrega_aux.sort(key=lambda pEntrega: manhattan_distance(almacen, pEntrega))
  grupo["puntosEntrega"] = pEntrega_aux[:8]
  grupo["almacen"] = almacen
  pEntrega_aux = pEntrega_aux[8:]
  grupos.append(grupo.copy())

  
  def coordenadas(node, size):
  x = node % size
  y = (node - x)/size
  return (int(x), int(y))
```
## Visualizacion de grupos de almaneces 
Previo a empezar a desarrollar las implementaciones o soluciones, creamos una funcion cuyo propósito principal es la de mostrar los grupos o secciones que hemos obtenido con las codificaciones anteriores, con el fin de que los algoritmos puedan implementarse de forma correcta e independiente, si perjudicar al grafo general. 

```python
def MostrarGrupo(L, labels=None, directed=False, weighted=False, path=[],
             layout="sfdp"):
  g = gv.Digraph("G") if directed else gv.Graph("G")
  g.graph_attr["layout"] = layout; g.edge_attr["color"] = "red"; g.node_attr["color"] = "green"; 
  g.node_attr["width"] = "0.2"; g.node_attr["height"] = "0.2"; g.node_attr["fontsize"] = "9"; 
  g.node_attr["fontcolor"] = "black"; g.node_attr["fontname"] = "monospace"; 
  g.edge_attr["fontsize"] = "9"; g.edge_attr["fontname"] = "monospace"
  n = len(L)
  for u in range(n):
    g.node(str(u), labels[u] if labels else str(u))
  added = set()
  for v, u in enumerate(path):
    if(u == -1 or u == None): continue
    if u != None:
      if weighted:
        for vi, w in L[u]:
          if vi == v:
            break
        g.edge(str(u), str(v), str(w), dir="forward", penwidth="2.5", color="purple")
      else:
        g.edge(str(u), str(v), dir="forward", penwidth="2.5", color="purple")
      added.add(f"{u},{v}")
      added.add(f"{v},{u}")
  if weighted:
    for u in range(n):
      for v, w in L[u]:
        if not directed and not f"{u},{v}" in added:
          added.add(f"{u},{v}")
          added.add(f"{v},{u}")
          g.edge(str(u), str(v), str(w))
        elif directed:
          g.edge(str(u), str(v), str(w))
  else:
    for u in range(n):
      for v in L[u]:
        if not directed and not f"{u},{v}" in added:
          added.add(f"{u},{v}")
          added.add(f"{v},{u}")
          g.edge(str(u), str(v))
        elif directed:
          g.edge(str(u), str(v))
  return g
```


 ## IMPLEMENTACIONES
 Para la seccion de soluciones nos dividimos en 5, de tal manera que cada integrante pueda realizar su implementación propia. 

 > - Cabe resaltar que por cada algoritmo definido, se implementa en un grupo, seccion o ciudad previamente divida. 


 
### 1er Algoritmo  - DIJKSTRA  (Sebastian Hernandez)
```python 
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

#!.------------ Implementacion en una seccion o grupo-------

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
```
### 2do Algoritmo  - PRIM   (Jesús Romero)
```python 
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

 #!.------------ Implementacion en una seccion/ grupo /ciudad-------

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
```
 ### 3er Algoritmo - BFS(BREADTH FIRST SEARCH) - (Emmanuel Ticona)
```python 
def bfs(G,s):  
    P,Q={s:None},col.deque([s])  
    while Q:  
        u=Q.popleft()  
        for v in G[u]:  
            if v in P:continue  
            P[v]=u  
            Q.append(v)  
    return P

#!.------------ Implementacion en una seccion/ grupo /ciudad-------

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
```

 ### 4to Algoritmo DFS(DEPTH FIRST SEARCH)
```python 
def dfs(G):
    S,res=set(),[]

    def recurse(u):
        if u in S: return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)

    for u in G:
        recurse(u)
    res.reverse()

    return res

#!.------------ Implementacion en una seccion/ grupo /ciudad-------

  def dfs_grupo(grupo, plt=None, ciudad = 60):
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
  path = dfs(grafo)
  if(plt == None): return MostrarGrupo(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      a = coordenadas(int(label[i]), ciudad)
      b = coordenadas(int(label[path[i]]), ciudad)
      plt.plot([a[0], b[0]], [a[1], b[1]])
```



### 5to Algoritmo - UCS - (Manuel Aranguri)
```python 
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
        if not G.nodes[v]['visited']:
          w_uv = G.edges[u, v]['weight']
          f_v  = g_u + w_uv
          g_v  = G.nodes[v]['cost']
          if f_v < g_v:
            G.nodes[v]['cost'] = f_v
            G.nodes[v]['path'] = u
            hq.heappush(q, (f_v, v))

  path = [0]*G.number_of_nodes()
  for v, info in G.nodes.data():
    path[v] = info['path']

  return path

#!.------------ Implementacion en una seccion/ grupo /ciudad-------

 def ucs_grupo(grupo, plt=None, ciudad=60):
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
  path = UCS(grafo, len(nodelist) - 1)
  if(plt == None): return MostrarGrupo(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      a = coordenadas(int(label[i]), ciudad)
      b = coordenadas(int(label[path[i]]), ciudad)
      plt.plot([a[0], b[0]], [a[1], b[1]])

 ucs_grupo(grupos[23],None,60)
```
## DEMOSTRACION 

En esta parte final, de los 5 algoritmos propuestos, escogimos el Prim para poder demostrar la solución, expresando los puntos de entrega los cuales podrán ser alcanzados por los "vehículos" de cada almacén.
``` python
plt.subplots(figsize=(20, 20))
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
for grupo in grupos:
  prim_grupo(grupo, plt, 2800)
plt.scatter(almacenes[:, 0], almacenes[:, 1], color = "blue")
plt.scatter(pEntrega[:, 0], pEntrega[:, 1], color = "magenta")
```
![image](https://raw.githubusercontent.com/JesusRomeroRivera/cc41-tf-201910711-201910295-201911572-201910149-201914885/main/GrafoFinal/grafoVersionFinal.jpg)

 ## CONCLUSIONES
- Trabajar y evaluar distintos algoritmos nos permitio darnos cuenta de que problemas de esta magnitud, pueden tener varias de estas soluciones. 
- Piorizar la velocidad con la que uno u otro algoritmo tarda en realizar el camino, dividir las secciones, mostrar los puntos, etc. Nos brindo un panorma mas amplio acerca de como operan dichos algoritmos y que tan importante es el analisis de estos para soluciones de alta complejidad.
- El trabajo y el curso en general nos dio las bases necesarias para tener un mejor contexto del manejo de big data(como en nuestro caso de 2800 puntos), y asi experimentar y contrastar con diferentes casos y problemas. 

 ## VIDEO EXPOSICION
- https://www.youtube.com/watch?v=VHbs7vvOw7g

 ## BIBLIOFRAFÍA 
- Christofides, N. (1976). The vehicle routing problem. Revue française d'automatique, informatique, recherche opérationnelle. Recherche opérationnelle, 10(V1), 55-70.
- Conrad, R. G., & Figliozzi, M. A. (2011, May). The recharging vehicle routing problem. In Proceedings of the 2011 industrial engineering research conference (p. 8). IISE Norcross, GA.
- Eksioglu, B., Vural, A. V., & Reisman, A. (2009). The vehicle routing problem: A taxonomic review. Computers & Industrial Engineering, 57(4), 1472-1483.
- Toth, P., & Vigo, D. (Eds.). (2002). The vehicle routing problem. Society for Industrial and Applied Mathematics.




