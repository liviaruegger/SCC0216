"""
@File:   ex04.py
@Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
@Date:   2022-07-02

@Brief:  SCC0216 - Modelagem Computacional em Grafos
         Trabalho 04: Algoritmo de Dijkstra

         A distância d_ij entre qualquer par de vértices V_i e V_j de
         um grafo valorado pode ser determinada por meio do Algoritmo
         de Dijkstra. Seja M uma matriz tal que M_ij = d_ij. Faça um
         código para implementar o algoritmo de Dijkstra.
         A saída do seu programa é a matriz M exibida na tela.
         A entrada é um arquivo padrão em formato pajek.
"""


import heapq
import math


class Graph:
    
    def __init__(self, file_name) -> None:
        pajek_file = open(file_name, "r")
        lines = pajek_file.readlines()

        self.n_vertices = int(lines[0].split()[1])
        edges = [edge.rstrip() for edge in lines[2:] if edge != "\n"]

        self.adjacency_list = dict()

        for edge in edges:
            i, j, weight = edge.split(" ")
            self.add_node(int(i), int(j), int(weight))


    def add_node(self, i: int, j: int, weight: int) -> None:
        if i not in self.adjacency_list:
            self.adjacency_list[i] = []
        if j not in self.adjacency_list:
            self.adjacency_list[j] = []

        if j not in self.adjacency_list[i]:
            self.adjacency_list[i].append([weight, j])


    def dijkstra(self, src: int) -> list[float]:
        visited = set()
        dist = [math.inf] * self.n_vertices
        dist[src - 1] = 0

        queue = [(0, src)]
        heapq.heapify(queue)

        while queue:
            tmp, i = heapq.heappop(queue)
            visited.add(i)

            for current_dist, edge in self.adjacency_list[i]:
                new_dist = dist[i - 1] + current_dist
                if edge not in visited and new_dist < dist[edge - 1]:
                    dist[edge - 1] = new_dist
                    heapq.heappush(queue, (new_dist, edge))

        return dist

    
    def __build_distance_matrix(self) -> None:
        self.dist_matrix = []
        for i in range(1, self.n_vertices + 1):
            self.dist_matrix.append(self.dijkstra(i))

    
    def print_distance_matrix(self) -> None:
        self.__build_distance_matrix()
        
        max_len = [0] * self.n_vertices # max_len para cada coluna

        for i in range(self.n_vertices):
            for row in self.dist_matrix:
                curr_len = len(str(row[i]))
                if curr_len > max_len[i]:
                    max_len[i] = curr_len

        for row in self.dist_matrix:
            i = 0
            for dist in row[:-1]: # Vai até o penúltimo elemento
                print(f"{str(dist).rjust(max_len[i])} ", end='')
                i += 1
            print(str(row[-1]).rjust(max_len[self.n_vertices - 1]))


file_name = input()
G = Graph(file_name)
G.print_distance_matrix()
