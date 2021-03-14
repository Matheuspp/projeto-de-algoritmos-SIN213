import template

class Node:
    """ Node base para uma estrutura de dados"""
    def __init__(self, dado=0, prox=None, ant=None):
        self.dado = dado
        self.prox = prox
        self.ant = ant

    def __repr__(self):
        return f"{self.dado}"

class ListaCircularDupEncadeada:
    "lista circular duplamente encadeada"

    def __init__(self):
        self.primeiro = None
    
    def retornar_node(self, posicao):
        atual = self.primeiro
        # ### percorrer node e encontrar a posição desejada
        for i in range(posicao):
            atual = atual.prox
            if atual == self.primeiro:
                return None
        return atual

    def inserir_proximo(self, ref_node, novo_node):
        novo_node.ant = ref_node
        novo_node.prox = ref_node.prox
        novo_node.prox.ant = novo_node
        ref_node.prox = novo_node
 
    def inserir_antes(self, ref_node, novo_node):
        self.inserir_proximo(ref_node.ant, novo_node)
 
    def inserir_fim(self, novo_node):
        if self.primeiro is None:
            self.primeiro = novo_node
            novo_node.prox = novo_node
            novo_node.ant = novo_node
        else:
            self.inserir_proximo(self.primeiro.ant, novo_node)
 
    def inserir_inicio(self, novo_node):
        self.inserir_fim(novo_node)
        self.primeiro = novo_node

    def busca(self, chave, N):
        # ### iniciar a busca a partir de 0 e N/2 ao mesmo tempo
        node_meio = self.retornar_node(N//2)
        parada = (N//2)+1

        for i in range(parada):
            parte1 = self.primeiro
            parte2 = node_meio

            if parte1.dado == chave:
                return parte1
            
            if parte2.dado == chave:
                return parte2
        return None        

    def imprimir(self, N):
        for i in range(N):
            print(f"node [{i}]: {self.retornar_node(i).dado}")

    def imprimir_recursivo(self):
        if self.primeiro is None:
            return
        atual = self.primeiro
        while True:
            print(f"node data: {atual.dado}")
            atual = atual.prox
            if atual == self.primeiro:
                break

if __name__ in '__main__':
    # ### carregando dados do template
    arranjo = template.arranjo

    lista_circular = ListaCircularDupEncadeada()
    
    # ### populando a lista circular 
    for item in arranjo:
        novo_node = Node(dado=item)
        lista_circular.inserir_inicio(novo_node)

    #lista_circular.imprimir(len(arranjo))
    #lista_circular.imprimir_recursivo()

    node = lista_circular.busca(38, len(arranjo))
    print(node.prox)
    
