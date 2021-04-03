from collections import defaultdict 
 
class Graph:
 
    # Constructor
    def __init__(self):
 
        self.graph = defaultdict(list)
 
    # ### adicionar borda grafo
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # ### Busca em profundidade
    def DFSUtil(self, v, visited):
 
        # ### marcar node atual como visitado
        visited.add(v)
        print(v, end=' ')
 
        # ### Todas as vertices adjacentes
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # ### recursive DFSUtil()
    def DFS(self, v):
 
        visited = set()

        self.DFSUtil(v, visited)
 
if __name__ in '__main__':
    # ### criar grafo
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    g.DFS(2)