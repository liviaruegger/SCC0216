"""
@File:   ex03b.py
@Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
@Date:   2022-06-10

@Brief:  SCC0216 - Modelagem Computacional em Grafos
         Trabalho 03: Busca em profundidade (Depth First Search)

         Faça um código para realizar uma busca em profundidade.
         A saída deve indicar se o grafo possui um ciclo ou não.
         A entrada é um arquivo padrão em formato pajek.
         
         Formato de saída: 'S' para ciclo presente ou 'N' para
         ciclo ausente.
"""


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


    def read_graph_from_pajek_file(self, file_name: str) -> None:

        # Abertura do arquivo .pajek
        pajek_file = open(file_name, "r")

        # Ler n
        first_line = pajek_file.readline()
        first_line = first_line.split()
        n = int(first_line[1])
        second_line = pajek_file.readline()

        # Ler arestas
        edges = []
        for line in pajek_file:
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
                if second_line == "*Edges\n":
                    adj[edge[1]].append(edge[0])

        # Atualizar objeto
        self.adjacency_list = adj
        self.n_of_vertices = n


    def __DFS(self, v: int) -> bool:
        self.colors[v] = "grey"

        for i in self.adjacency_list[v]:
            if self.colors[i] == "white":
                if self.__DFS(i):
                    return True
            elif self.colors[i] == "grey":
                return True

        self.colors[v] = "black"

        return False


    def is_cyclic(self) -> bool:
        self.colors = ["white"] * self.n_of_vertices
        
        for v in range(self.n_of_vertices):
            if self.colors[v] == "white":
                if self.__DFS(v):
                    return True
        
        return False


def main(): 
    G = Graph()

    file_name = input()
    G.read_graph_from_pajek_file(file_name)

    print("S") if G.is_cyclic() else print("N")
    

main()
