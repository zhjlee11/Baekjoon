from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

class Grid:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = {}
        self.adj = {}
        self.will_melt = []
        self.t = 0


    def get(self, x, y):
        if (x, y) in self.data.keys():
            return self.data[(x, y)]
        else:
            return None

    def set(self, x, y, value):
        self.data[(x, y)] = value

    def reset_adj(self):
        for (x, y) in self.data.keys():
                self.adj[(x, y)] = 0

    def isEmpty(self):
        return True not in self.data.values()

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
                if self.adj[(dx, dy)] < 2:
                    self.adj[(dx, dy)] += 1
                    if self.adj[(dx, dy)] >= 2:
                        self.will_melt.append((dx, dy))
    def get_neighboor(self, x, y, filter):
        result = []
        target = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

        for (dx, dy) in target:
            if self.get(dx, dy) == filter:
                result.append((dx, dy))
        return result

    def count_adj(self, V=(1, 1)):
        queue = deque()
        queue.append(V)
        visited = [V]

        while queue:
            V = queue.popleft()
            self.melt_adj_cheese(*V)
            target = self.get_neighboor(*V, filter=False)
            for n in target:
                if n not in visited:
                    queue.append(n)
                    visited.append(n)

    def melt(self):
        self.t += 1
        self.count_adj()
        for n in self.will_melt:
            self.set(*n, False)
        self.reset_adj()
        self.will_melt = []

n, m = map(int, input().split(" "))

grid = Grid(n, m)

for y in range(1, n+1):
    inp = map(int, input().split(" "))
    for ind, v in enumerate(inp):
        x = ind + 1
        if v==1:
            grid.set(x, y, True)
        else :
            grid.set(x, y, False)
        grid.adj[(x, y)] = 0

while not grid.isEmpty():
    grid.melt()
    # print("\n")
    # grid.visualize()
    # print("\n")

print(f"{grid.t}")