int numNodes = ...;
int numEdges = ...;

// Represents an edge in the graphe
tuple Edge {
    int node1;
    int node2;
}

// Loads all edges present in the graph
{Edge} edges = ...;

// Stores the solution for all nodes
dvar int+ nodeSolution[1..numNodes];

// Minimize the sum of all nodes
minimize max (i in 1..numNodes) nodeSolution[i];

// Each edge needs to be adjacent to at least one node with a value of 1
subject to {
    forall (edge in edges) {
        // Both nodes edge different color
        nodeSolution[edge.node1] != nodeSolution[edge.node2];
    }

}


// Printing solution
execute {
    for(var i = 1; i <= numNodes; i++) {
        writeln("Knoten ", i, ": ", nodeSolution[i]);

    }
}