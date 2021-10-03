# Algoritmo Depth-First Search (DFS)
----
## Pseudocódigo en alto nivel
----
	DFS(G, u)
    u.visitado = true
    PARA CADA v EN G.Adj[u]
        SI v.visitado == false
            DFS(G,v)
            
    iniciar() {
      PARA CADA u EN G
        u.visitado = false
      PARA CADA u EN G
        DFS(G, u)
    }
## Análisis
----
- BFS es un algoritmo de desplazamiento en que se empieza a desplazar desde un nodo específico uno por uno explorando todos los nodos vecinos.
- En la función iniciar() se corre la función DFS en todos los nodos, ya que el grafo podría tener dos partes diferentes desconectadas.
- La función principal de este algoritmo es averiguar si es que un nodo existe en el grafo.
- Teóricamente, DFS se utiliza para atravesar un grafo entero, lo que toma un tiempo de O(|V| + |E|) donde |V| es el número de vértices y |E| es el número de bordes.
- Si no se marcaran los nodos como visitados, se podría visitar el mismo nodo varias veces lo que podría ocasionar que se llegue a un bucle infinito.
