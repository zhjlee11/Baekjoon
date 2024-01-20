# https://www.acmicpc.net/problem/1197
from copy import deepcopy
import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def KrusaklAlgorith(graph, V, E):
    parent = {i:i for i in range(1, V + 1)}
    sorted_graph = dict(sorted(graph.items(), key=lambda item: item[1]))
    weight = 0
    for (a, b), w in sorted_graph.items():
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            weight += w
    return weight


if __name__=="__main__":
    V, E = map(int, input().split(" "))
    graph = {}
    for _ in range(E):
        A, B, C = map(int, input().split(" "))
        graph[(A, B)] = C

    print(f"{str(KrusaklAlgorith(graph, V, E))}")