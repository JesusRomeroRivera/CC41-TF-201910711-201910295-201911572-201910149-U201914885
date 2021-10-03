# Algoritmo DE busqueda de costo unforme (UCS)
----
## Pseudocódigo
----
        algoritmo UCS(gráfico, raíz, objetivo)
        nodo: = raíz, costo = 0
        frontera: = cola de prioridad que contiene solo el nodo
        explorado: = conjunto vacío
        hacer
            si la frontera esta vacia
            falla de retorno
            nodo: = frontera.pop ()
            si el nodo es el objetivo
            solución de devolución
            explored.add (nodo)
            para cada uno de los vecinos n del nodo
            si n no está explorado
                si n no está en la frontera
                frontier.add (n)
                de lo contrario, si n está en la frontera con un costo más alto
                reemplace el nodo existente con n

## Análisis
----
- UCS es un algoritmo que se utiliza para recorrer sobre grafos el camino más corto entre 2 nodos: raíz y destino. Asismismo, se encuentra en la categoríad de algoritmos de búszqueda no informada. La búsqueda inicia por el nodo raíz y pasa al siguiente nodo que tiene menor costo total desde la raíz. 

- Lo que caracteriza a este algoritmo esque a diferencia de BFS, este emplea una cola de prioridad. Donde, el elemento de menor costo se encuentra al frente.

- El tiempo para el caso peor y uso de memoria O(b1 + C*/ε), donde C* es el costo de la solución óptima y b es el factor de ramificación. Asimismo, podemos interpretar C*/ε como el número de pasos que le tomaría llegar a la meta, considerando que cada una de esas acciones es de costo mínimo. Cuando todos los costos entre los nodos son iguales, esto se convierte en O(b^d + 1)^2​

- En lo que a calidad se refiere, el algoritmo nos retorna la solución óptima. Además presenta la carácterística de ser un algoritmo completo. 
