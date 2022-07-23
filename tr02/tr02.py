"""
@File:   tr02.py
@Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
@Author: Johnny Batista da Silva (N.USP 11371350)
@Date:   2022-07-23

@Brief:  SCC0216 - Modelagem Computacional em Grafos
         Projeto 02: Algoritmo de Prim

         Faça um código para implementar o algoritmo de Prim
         (ou Kruskal). A entrada é o nome de um arquivo padrão
         em formato pajek. A saída do seu programa deve ser a 
         soma de pesos de arestas de árvore geradora minima.
"""


import sys


class Graph:
    
    def __init__(self, file_name: str) -> None:
        """
        Lê um grafo a partir de um arquivo padrão em formato
        pajek, construindo sua representação tanto em forma
        de matriz quanto em forma de lista de adjacências.
        Também constrói, utilizando o algoritmo de Prim, a
        sua árvore geradora mínima.
        """
        pajek_file = open(file_name, "r")
        lines = pajek_file.readlines()

        self.n_vertices = int(lines[0].split()[1])
        edges = [edge.rstrip() for edge in lines[2:] if edge != "\n"]

        self.adjacency_list = dict()
        self.adjacency_matrix = [
            [0 for j in range(self.n_vertices)] for i in range(self.n_vertices)
        ]

        for edge in edges:
            i, j, weight = edge.split(" ")

            self.add_node(int(i), int(j), int(weight))
            self.add_node(int(j), int(i), int(weight))

            self.adjacency_matrix[int(i) - 1][int(j) - 1] = int(weight)
            self.adjacency_matrix[int(j) - 1][int(i) - 1] = int(weight)

        self.MST = self.prim()


    def add_node(self, i: int, j: int, weight: int) -> None:
        """
        Adiciona um novo nó à matriz de adjacência.
        """
        if i not in self.adjacency_list:
            self.adjacency_list[i] = []
        if j not in self.adjacency_list:
            self.adjacency_list[j] = []

        if j not in self.adjacency_list[i]:
            self.adjacency_list[i].append([weight, j])


    def _min_key(self, key: list[int], MST_set: list[bool]) -> int:
        """
        Encontra o vértice com menor distância, entre um
        conjunto de vértices que ainda não foi incluído
        na árvore SPT.
        """
        min = sys.maxsize  # Inicializa com "infinito"

        for v in range(self.n_vertices):
            if key[v] < min and MST_set[v] == False:
                min = key[v]
                min_index = v

        return min_index


    def prim(self) -> list[int]:
        """
        Constrói a árvore geradora mínima do grafo
        a partir da matriz de adjacência.
        """
        parent = [None] * self.n_vertices

        key = [sys.maxsize] * self.n_vertices
        MST_set = [False] * self.n_vertices

        key[0] = 0
        parent[0] = -1

        for i in range(self.n_vertices):
            u = self._min_key(key, MST_set)
            MST_set[u] = True

            for v in range(self.n_vertices):
                if (
                    self.adjacency_matrix[u][v] > 0
                    and MST_set[v] == False
                    and key[v] > self.adjacency_matrix[u][v]
                ):
                    key[v] = self.adjacency_matrix[u][v]
                    parent[v] = u

        return parent


    def sum_MST(self) -> int:
        """
        Calcula a soma de pesos das arestas de árvore
        geradora minima.
        """
        weight_sum = 0
        for i in range(1, self.n_vertices):
            weight_sum += self.adjacency_matrix[i][self.MST[i]]

        return weight_sum


file_name = input()
G = Graph(file_name)
print(G.sum_MST())
