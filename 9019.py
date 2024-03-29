# https://www.acmicpc.net/problem/9019
from collections import deque
import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")


class Data:
    def __init__(self, num, rec=""):
        self.num = num
        self.record = rec

    def __int__(self):
        return self.num

    def __str__(self):
        return self.record

    def __eq__(self, other):
        return self.num == other.num


def D(num):
    return (2 * num) % 10000


def S(num):
    return 9999 if num <= 1 else num - 1


def L(num):
    d1 = num // 1000
    rest = num % 1000
    return 10 * rest + d1


def R(num):
    rest = num // 10
    d4 = (num % 10)
    return 1000 * d4 + rest


def getAdjacent(data, targets):
    new_record_num = len(data.record) + 1
    candidate = {"D": D(data.num), "S": S(data.num), "L": L(data.num), "R": R(data.num)}
    result = {}

    for c, k in candidate.items():
        if targets[k] is not None:
            if new_record_num >= len(targets[k].record):
                continue
        result[c] = Data(k, rec=data.record + c)

    return result


def bfs(A, B, result=None):
    start = Data(A)
    visited = [None for _ in range(0, 10001)]
    visited[A] = start
    queue = deque([start])

    while queue:
        V = queue.popleft()

        if len(result) if result is not None else 10001 > len(str(V)):
            if int(V) == B:
                result = str(V)
            else:
                for c, new_data in getAdjacent(V, visited).items():
                    queue.append(new_data)
                    visited[new_data.num] = new_data

    return result


try_num = int(input())
experiment = []
for _ in range(try_num):
    experiment.append(list(map(int, input().split())))

for A, B in experiment:
    print(bfs(A, B))
