def biggest_descendent(graph, root, value):

    biggest = {}

    def dfs(u):
       
        biggest[u] = value[u]

       
        for v in graph.neighbors(u):
            child_biggest = dfs(v)

            if child_biggest > biggest[u]:
                biggest[u] = child_biggest

        return biggest[u]

    dfs(root)
    return biggest