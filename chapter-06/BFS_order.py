
# This BFS search in the entire list, just for study purposes
def BFS(listaAdj: dict[int, list[int]], v):
    
    q = []
    q.append(v)

    analisados = []



    while q:

        v = q.pop(0)
        for adj in listaAdj[v]:
            if adj not in q and adj not in analisados:
                q.append(adj)

        analisados.append(v)


    vertices_grafo = list(listaAdj.keys())
    
    # tratando vértices de um grafo desconexo
    for v in vertices_grafo:
        if v not in analisados:
            analisados.append(v)


    print(analisados)


if __name__ == "__main__":
    grafo = {
    0: [1, 4, 5],  # ok
    1: [0, 2, 5, 8, 10],
    2: [1, 3, 6, 11],
    3: [2, 7, 10],
    4: [0, 5, 8],
    5: [0, 1, 4, 6, 9],
    6: [2, 5, 7, 10],
    7: [3, 6, 11],
    8: [1, 4, 9],
    9: [5, 8, 10],
    10: [1, 3, 6, 9, 11],
    11: [2, 7, 10],
}


    BFS(grafo, 0)