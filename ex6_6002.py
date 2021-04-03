from collections import defaultdict
 
# ### grafo
class Graph:
 
    # Constructor
    def __init__(self):

        self.graph = defaultdict(list)
 
    # ### adicionar borda grafo
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # ### Busca em largura
    def BFS(self, s):
 
        # ### marcar node atual como visitado
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
if __name__ in "__main__":
    # ### criar grafo
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(3, 2)
 
    g.BFS(2)