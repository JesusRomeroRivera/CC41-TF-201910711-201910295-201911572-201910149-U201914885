#Algoritmo de Dijkstra
----
##Pseudocódigo del algoritmo
----

```
funcion dijkstra(G, S)
    para u ∈ V[G] hacer
           distancia[u] = infinito
           previo[u] = NULL
           visto[u] = false
       distancia[s] = 0
       adicionar (cola, (s, distancia[s]))
       mientras cola no este vacia
           u = extraer_mínimo(cola)
           visto[u] = true
           por cada v en adyacencia[u]
               si  no visto[v] y distancia[v] > distancia[u] + peso (u, v) 
                    distancia[v] = distancia[u] + peso (u, v)
                    padre[v] = u
                    adicionar(cola,(v, distancia[v])) 
```

##Posible Análisis Asintótico
----
El tiempo de ejecución (orden de complejidad) del algoritmo de Dijkstra:

- La cola (de prioridad) toma un tiempo O(V). Primero se agregan los vértices del grafo a la cola, tras estar completada, el ciclo while es ejecutado por cada vértice.
- Dentro del ciclo while, cada llamada a extraer_minimo toma un tiempo O(logV).
- En conjunto estas dos partes toman un tiempo O(Vlog(V))
- El ciclo for es ejecutado por cada arista, y en cada uno, la funcion adicionar toma un tiempo O(Elog(V)).
- Luego, el tiempo de ejecución combinado es O((V+E)log(V)).
- La complejidad computacional, considerando que el algoritmo tiene n-1 iteraciones como maximo por los vertices añadidos, y que en cada iteracion se identifica un vertice (n-1) y se realiza una suma y comparación, en cada iteración se tienen 2(n-1) operaciones. 
- Entonces el algoritmo realiza O(n^2) operaciones

