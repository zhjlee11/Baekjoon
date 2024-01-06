from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

class Grid:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[False for _ in range(self.m)] for _ in range(self.n)]
        self.adj = [[0 for _ in range(self.m)] for _ in range(self.n)]
        self.t = 0
        self.previous_cheese_num = 0

    def get(self, x, y):
        if 1 <= x <= self.m and 1 <= y <= self.n:
            return self.data[y-1][x-1]
        else:
            return None

    def set(self, x, y, value):
        if 1 <= x <= self.m and 1 <= y <= self.n:
            self.data[y-1][x-1] = value
        else:
            assert "Strange Position"

    def reset_adj(self):
        self.adj = [[0 for _ in range(self.m)] for _ in range(self.n)]

    def isEmpty(self):
        result = True
        for row in self.data:
            if True in row:
                result = False
        return result

    def count_cheese(self):
        self.previous_cheese_num = 0
        for row in self.data:
            for ele in row:
                if ele:
                    self.previous_cheese_num+=1

    def visualize(self):
        for y in range(1, self.n + 1):
            line = f"{1 if self.get(1, y) else 0}"
            for x in range(2, self.m + 1):
                line += f" {1 if self.get(x, y) else 0}"
            print(line + "\n")

    def melt_adj_cheese(self, x, y):
        if not self.get(x, y):
            target = self.get_neighboor(x, y, filter=True)
            for (dx, dy) in target:
                self.adj[dy-1][dx-1] += 1

    def get_neighboor(self, x, y, filter):
        result = []
        target = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

        for (dx, dy) in target:
            if self.get(dx, dy) == filter:
                result.append((dx, dy))
        return result

    def count_adj(self, v=(1, 1)):
        queue = deque()
        queue.append(v)
        visited = [[False for _ in range(self.m)] for _ in range(self.n)]

        while queue:
            v = queue.popleft()
            self.melt_adj_cheese(*v)
            target = self.get_neighboor(*v, filter=False)
            for (x, y) in target:
                if not visited[y-1][x-1]:
                    queue.append((x, y))
                    visited[y-1][x-1] = True

    def melt(self):
        self.t += 1
        self.count_cheese()
        self.count_adj()
        for x in range(2, self.m):
            for y in range(2, self.n):
                if self.adj[y-1][x-1] >= 1:
                    self.set(x, y, False)
        self.reset_adj()


n, m = map(int, input().split(" "))
grid = Grid(n, m)
for y in range(1, n+1):
    inp = map(int, input().split(" "))
    for ind, v in enumerate(inp):
        if v==1:
            grid.set(ind + 1, y, True)

while not grid.isEmpty():
    grid.melt()
    # print("\n")
    # grid.visualize()
    # print("\n")


print(f"{grid.t}\n{grid.previous_cheese_num}")