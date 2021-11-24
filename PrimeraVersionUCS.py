def ucs(G, S, E, w=None):
    frontier = PriorityQueue()
    frontier.put((0, start)) 
    visited = []

    while True:
        if frontier.empty():
            raise Exception("no encontrado")
        ucs_w, current_node = frontier.get()
        explored.append(current_node)

        if current_node == end:
            return

        for node in G[current_node]:
            if node not in visited:
                frontier.put((
                    ucs_w + ucs_weight(current_node, node, w),
                    node
                ))

