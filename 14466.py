# https://www.acmicpc.net/problem/1309
import sys
input = sys.stdin.readline
print = sys.stdout.write

def getAdjCell(V):
    candidate = [(V[0]+1, V[1]), (V[0]-1, V[1]), (V[0], V[1]+1), (V[0], V[1]-1)]
    result = []
    for c in candidate:
        if 1 <= c[0] <= N and 1 <= c[1] <= N:
            if (V, c) not in unconnected and (c, V) not in unconnected:
                result.append(c)
    return result

def bfs(V):
    area = []
    queue = [V]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[V[1]-1][V[0]-1] = True #방문처리
    while queue:
        V = queue.pop(0)
        area.append(V)
        for c in getAdjCell(V):
            if visited[c[1]-1][c[0]-1] == False:
                queue.append(c)
                visited[c[1]-1][c[0]-1] = True # 방문처리
    return area

if __name__ == "__main__":
    N, K, R = map(int, input().split(" "))

    unconnected = []
    for _ in range(R):
        r1, c1, r2, c2 = map(int, input().split(" "))
        unconnected.append(((r1, c1), (r2, c2)))

    for cow in range(K):
        r, c = map(int, input().split(" "))
        area = bfs((r, c))