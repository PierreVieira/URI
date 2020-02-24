"""
Autor: Pierre Vieira
Data da submissão: 24/02/2020 15:12:27
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Referência para o nó à esquerda
        self.right = None  # Referência para o nó à direita

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:  # se o usuário especificou o nó
            node = TreeNode(data)
            self.root = node  # Raiz da árvore
        else:
            self.root = None


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        """
        Faz a inserção de um nó em uma árvore binária de busca.
        :param value: valor a ser inserido.
        :return: None
        """
        no = TreeNode(value)
        parent = None  # determina o pai do novo nó a ser inserido
        x = self.root  # x começa na raiz
        cont_altura = 0
        while x is not None:  # enquanto x diferente de vazio
            parent = x
            cont_altura += 1
            if value < x.data:  # se o valor informado é menor que x
                x = x.left  # desça pela direita
            else:  # se não
                x = x.right  # desça pela esquerda
        if parent is None:  # se não tinha nada na árvore (sem raíz)
            self.root = no  # defina uma nova raíz
        elif value < parent.data:  # se o valor é menor que o parent
            parent.left = no  # insira o nó à esquerda do parent
        else:  # se não
            parent.right = no  # insira o nó à direita do parent
        lista_alturas.append((cont_altura, no.data))


qtde_casos_teste = int(input())


def saida():
    print('Case {}:'.format(c + 1))
    for d in range(len(lista_alturas) - 1):
        print(lista_alturas[d][1], end=' ')
    print(lista_alturas[len(lista_alturas) - 1][1], end='\n\n')


for c in range(qtde_casos_teste):
    lista_alturas = []
    n = int(input())
    arvore_binaria_de_busca = BinarySearchTree()
    for v in map(int, input().split()):
        arvore_binaria_de_busca.insert(v)
    lista_alturas.sort()
    saida()
