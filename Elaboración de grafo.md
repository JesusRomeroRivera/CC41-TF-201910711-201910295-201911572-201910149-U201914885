```
import csv
import numpy as np
import matplotlib.pyplot as plt
def write_csv(headers, fields, filename):
  with open(filename, 'w') as f:   
    write = csv.writer(f)
    if headers != None: write.writerow(headers)
    write.writerows(fields)
def read_csv(filename):
  csv_file = list()
  with open(filename) as File:
    reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for i in reader:
        if i[0] != 'x':
          i[0], i[1] = int(i[0]), int(i[1])
          csv_file.append(i)
  csv_file.sort(key = lambda x: (x[0], x[1]))
  return csv_file
almacenes = read_csv("almacenes.csv")
puntos_entrega = read_csv("puntos_entrega.csv")
x, y = np.array(almacenes).T
x2, y2 = np.array(puntos_entrega).T
mat.figure(figsize=(15, 15))
mat.scatter(x,y, 2, c="red")
mat.scatter(x2,y2, 2, c="blue")
mat.show()
for i, _ in enumerate(almacenes):
  almacenes[i].append("A")
for i, _ in enumerate(puntos_entrega):
  puntos_entrega[i].append("C")
city = list()
city.extend(almacenes)
city.extend(puntos_entrega)
city.sort(key = lambda x: (x[0], x[1]))
graph = [[] for _ in city]
for i, _ in enumerate(city):
  for j, _ in enumerate(city):
    if i == j: continue
    if city[i][0] == city[j][0] or city[i][1] == city[j][1]: graph[i].append(j)
write_csv(['x', 'y', 'type'], city, 'city.csv')
write_csv(None, graph, 'graph.csv')
```
