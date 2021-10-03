# **Algoritmo BFS (Breadth First Search)**

## Pseudocódigo

``` [python]
  metodo BFS(Grafo,origen):
      creamos una cola I
      agregamos origen a la cola I
      marcamos origen como visitado
      mientras I no este vacío:
          sacamos un elemento de la cola I llamado x
          para cada vertice y adyacente a x en el Grafo: 
              si z no ah sido visitado:
                 marcamos como visitado z
                 insertamos z dentro de la cola I
```


## Análisis asintótico

- El algoritmo DFS es unAlgoritmo recursivo, Se necesita una pila de trabajo recursiva, por lo que su complejidad espacial es O (| V |). 
- El proceso de atravesar el gráfico es esencialmente el proceso de encontrar sus puntos vecinos para cada vértice.
- El tiempo que lleva depende de la estructura de almacenamiento utilizada. Cuando se representa mediante una matriz de adyacencia, 
  el tiempo necesario para encontrar el punto adyacente de cada vértice es O (| V |), por lo que la complejidad del tiempo total es O (| V * V |). 
- Cuando se representa mediante una lista de adyacencia, el tiempo requerido para encontrar los puntos vecinos de todos los vértices es O (| E |), 
  y el tiempo requerido para acceder a los vértices es O (| V |). En este momento, la complejidad de tiempo total es O (| V | + | E |).
