def manhattan_distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])
  
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
