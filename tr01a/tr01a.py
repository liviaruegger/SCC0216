"""
@File:   tr01a.py
@Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
@Author: Johnny Batista da Silva (N.USP 11371350)
@Date:   2022-07-02

@Brief:  SCC0216 - Modelagem Computacional em Grafos
         Projeto 01

         Uma coloração de um grafo não dirigido é uma rotulação dos
         vértices tal que os nós vizinhos não tenham as mesmas cores.
         No grafo descrito na entrada, o subconjunto dos vértices 
         [4,5,7,9,12,13,16,17,18,19,20] não é rotulável com uma única
         cor, porém é possível descartar um dos vértices mencionados
         e obter um novo subconjunto dos vértices, todos rotuláveis
         com uma única cor. Qual é esse vértice?
"""


import sys
from typing import List


class Graph:

    def __init__(self, adjacency_list: List[List[int]] = None) -> None:
        if adjacency_list:
            self.adjacency_list = adjacency_list
            self.n_of_vertices = len(adjacency_list)

    
    def __str__(self) -> str:
        to_string = ""
        for i in range(len(self.adjacency_list)):
            to_string += "Vertice " + str(i) + ": " + str(self.adjacency_list[i]) + "\n"
        return to_string


    def read_graph_from_stdin(self) -> None:
        # Ler n
        first_line = input()
        first_line = first_line.split()
        n = int(first_line[1])
        second_line = input().strip()

        # Ler arestas
        edges = []
        for line in sys.stdin:
            vertice = []
            for var in line.split():
                vertice.append(int(var) - 1)
            edges.append(vertice)

        # Criar o grafo vazio
        adj = []
        for i in range(n):
            adj.append([])

        # Construir o grafo
        for edge in edges:
            if len(edge) == 2:
                adj[edge[0]].append(edge[1])
                if second_line == "*Edges":
                    adj[edge[1]].append(edge[0])

        # Atualizar objeto
        self.adjacency_list = adj
        self.n_of_vertices = n


def main(): 
    G = Graph()
    G.read_graph_from_stdin()

    # Informação dada no enunciado:
    vertices_to_check = [4, 5, 7, 9, 12, 13, 16, 17, 18, 19, 20]

    # Atualizando para o índice começando em 0
    for i in range(len(vertices_to_check)):
        vertices_to_check[i] -= 1

    # Encontrar o vértice que deve ser retirado
    for vertice in vertices_to_check:
        intersection = list(set(vertices_to_check) & set(G.adjacency_list[vertice]))
        if len(intersection) == 2:
            print(vertice + 1)
 

main()
