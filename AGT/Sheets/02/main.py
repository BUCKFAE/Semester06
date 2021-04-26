def checkCircle(G, start):

    # Stores nodes in order of visit
    vistited = []

    vistited.append(start)

    # Index of the current node in visted
    counter = 0

    while len(vistited) != G.node_count:
        
        # Remove next node form current adj list
        adj = vistited[counter].adjacent[0]

        # Continue if no adjacent nodes
        if adj == nil:
            counter -= 1
            continue

        vistited[counter].adj.remove(adj)


        # If we landed on a node we visited before
        if adj.vistited is True:
            return True

        # Storing that we know the node
        adj.visited = True

        counter += 1
        vistited.append(adj)

    return False