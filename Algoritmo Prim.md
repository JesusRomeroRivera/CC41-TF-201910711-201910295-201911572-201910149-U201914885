# Algoritmo de Prim

El algoritmo de Prim encuentra un árbol recubridor minimo, un subconjunto de aristas que conforman un árbol
con todos los vértices. 

## Pseudocodigo
``` [python]
AlgoritmoPrim (Grafo G)
  for each x in V[G] do
    Set vértices al infinito
    Agregar cada vértice
  distance[x] = 0
  Update cambios en el vértice
  while [No esté vacío] do
    Set valor x
    for each v adjacent to 'x' do
      if ([v es prioridad] y [distancia > peso) so
        Set vértices a X
        Update cambios en el vértice
```

## Funcionamiento del algoritmo
1. Elegir un vértice cualquiera => Vértice de partida.
2. Seleccionar la arista que tenga menor peso adyacente al vértice de partida -> Se selecciona el otro vértice en el que colinda dicha arista.
3. Repetir el paso anterior si => La arista elegida tenga conexión con un vértice ya seleccionado y otro que no.
5. El algoritmo finaliza cuando todos los vértices del grafo han sido seleccionados.

## Analisis asintotico del algoritmo
La implementación del algoritmo de Prim contempla un tiempo de complejidad O(n^2). 
Sin embargo, en el pseudocodigo propuesto la implementación es a traves de un montículo. Por ello, la complejidad de nuestro algoritmo sería O(log(n)).
