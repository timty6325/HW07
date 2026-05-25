def cluster(graph, weights, level):

    visited = set()
    clusters = set()

    def dfs(u, current_cluster):
        visited.add(u)
        current_cluster.add(u)

        for v in graph.neighbors(u):
            if v not in visited and weights(u, v) >= level:
                dfs(v, current_cluster)

    for node in graph.nodes:
        if node not in visited:
            current_cluster = set()
            dfs(node, current_cluster)
            clusters.add(frozenset(current_cluster))

    return frozenset(clusters)