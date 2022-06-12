"""
@File:   ex01.py
@Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
@Date:   2022-04-11

@Brief:  SCC0216 - Modelagem Computacional em Grafos
         Trabalho 01: Geração de matriz de adjacência do modelo Erdös–Rényi

         Dada uma entrada [N, p], onde N representa o número de vértices de
         um grafo não direcionado e p é um parâmetro 0 < p < 1 que está
         relacionado a probabilidade de uma conexão existir entre 2 vértices,
         faça uma função que retorne a matriz de adjacência M de um grafo no
         modelo Erdös-Renyi dado os parametros N e p.
"""

import random
import numpy 

def random_graph(N, p):
    adjacency_matrix = numpy.zeros((N, N), dtype=int)

    for i in range(N):
        for j in range(i):
            x = random.random()
            if x > p:
                adjacency_matrix[i][j] = 1
                adjacency_matrix[j][i] = 1

    return adjacency_matrix


N = int(input("Digite N (inteiro): "))
p = float(input("Digite p (valor de ponto flutuante, 0 < p < 1): "))

print("\n\nMatriz de adjacência do grafo gerado (modelo Erdös-Renyi):\n")
print(random_graph(N,p))