# https://www.acmicpc.net/problem/7576
from collections import deque
import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x))

m, n = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
step_num = 0
farm = []
for i in range(n):
    farm.append(list(map(int, input().split())))


def getConnectedCell(x, y):
    candidate = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    result = []
    for pos in candidate:
        if 0 <= pos[0] <= m - 1 and 0 <= pos[1] <= n - 1:
            result.append(pos)
    return result


def isEnd(farm):
    for line in farm:
        if 0 in line:
            return False
    return True


def getStartPos(farm, m, n):
    result = []
    for x in range(m):
        for y in range(n):
            if farm[y][x] >= 1:
                result.append((x, y))
    return result


def step(farm, m, n, startPosList):
    global step_num
    queue = deque([*startPosList])
    for pos in startPosList:
        visited[pos[1]][pos[0]] = True

    while queue:
        V = queue.popleft()
        for pos in getConnectedCell(*V):
            if farm[pos[1]][pos[0]] == 0:
                farm[pos[1]][pos[0]] = farm[V[1]][V[0]] + 1
                step_num = max(step_num, farm[pos[1]][pos[0]])
            if farm[pos[1]][pos[0]] >= 1:
                if not visited[pos[1]][pos[0]]:
                    queue.append(pos)
                    visited[pos[1]][pos[0]] = True


step(farm, m, n, getStartPos(farm, m, n))
if not isEnd(farm):
    print("-1")
else:
    print(max(step_num-1, 0))