# https://www.acmicpc.net/problem/2178
import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split(" "))
maze = [[False for _ in range(m)] for _ in range(n)]
minLength = 0
for y in range(n):
    inp = map(int, list(input())[:-1])
    for x, v in enumerate(inp):
        if v==1:
            maze[y][x] = True
            minLength+=1

def getNearCell(x, y):
    global maze, m, n
    isValidCell = lambda x, y : 0<=x<m and 0<=y<n
    candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    result = []
    for candidate in candidates:
        if isValidCell(*candidate):
            if maze[candidate[1]][candidate[0]]:
                result.append(candidate)
    return result

def bfs(V=(0, 0)):
    global minLength
    queue = []
    visited = [[False for _ in range(m)] for _ in range(n)]

    heapq.heappush(queue, [1, V])
    visited[V[1]][V[0]] = True

    while queue:
        current_distance, V = heapq.heappop(queue) #방문 노드 제거
        if V[0]==m-1 and V[1]==n-1:
            minLength = min(minLength, current_distance)
        for (x, y) in getNearCell(*V):
            if visited[y][x] == False and current_distance+1 <= minLength:
                visited[y][x] = True
                heapq.heappush(queue, [current_distance+1, (x, y)])

bfs()

print(f"{minLength}")