# https://www.acmicpc.net/problem/4883
import sys

input = sys.stdin.readline
#print = sys.stdout.write

test_case = {}
c = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        res = []
        for _ in range(N):
            res.append(list(map(int, input().split())))
        test_case[c] = res
        c += 1

min_t = 0
min_value = 1000000
for t, graph in test_case.items():
    value = 0
    value += (graph[0][1] + graph[-1][1])
    middle = graph[1:-1]
    prev_node = 1



    if min_value > value:
        min_t = t
        min_value = value

print(f"{min_t}. {min_value}")