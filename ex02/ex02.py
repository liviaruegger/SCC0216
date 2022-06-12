"""
@File:   ex02.py
@Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
@Date:   2022-05-27

@Brief:  SCC0216 - Modelagem Computacional em Grafos
         Trabalho 02: Busca em largura (Breadth First Search)

         A distância d_ij entre qualquer par de vértices V_i e V_j de um
         grafo não dirigido pode ser determinada por meio de uma busca em
         largura. Faça um programa que receba um grafo (arquivo padrão em
         formato pajek), realize uma busca em largura e apresente como saída
         a matriz M, tal que M_ij = d_ij.
"""

import sys

def BFS(G, n, start_v, colors):
    ''' Algoritmo de busca em largura '''
    dist = [-1] * n # A distância inicial é infinita (será representada por -1)
    
    v = start_v
    colors[v] = "grey"
    dist[v] = 0
    queue = [v]

    while len(queue) > 0:
        v = queue[0]
        queue.pop(0)

        if colors[v] != "black":
            colors[v] = "black"
        
        for w in G[v]:
            if colors[w] == "white":
                colors[w] == "grey"
                dist[w] = dist[v] + 1
                queue.append(w)
        
    return dist


''' Ler n '''
first_line = input()
first_line = first_line.split()
n = int(first_line[1])
input() # Ignora segunda linha

''' Ler arestas '''
edges = []
for line in sys.stdin:
    vertice = []
    for var in line.split():
        vertice.append(int(var) - 1)
    edges.append(vertice)

''' Criar o grafo vazio'''
G = []
for i in range(n):
    G.append([])

''' Construir o grafo '''
for edge in edges:
    G[edge[0]].append(edge[1])
    G[edge[1]].append(edge[0])

''' Imprimir matriz de distâncias '''
for i in range(n):
    for dist in BFS(G, n, i, ["white"] * n):
        print(dist, end=" ")
    print()