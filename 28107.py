# https://www.acmicpc.net/problem/28107
import sys
from collections import deque
input = sys.stdin.readline
#print = sys.stdout.write

N, M = map(int, input().split())
consumer_menu = []
for _ in range(N):
    lis = list(input().split())
    consumer_menu.append(set(lis[1:]))
sushi_num = list(input().split())

sushi_dict = {i:deque([]) for i in sushi_num}
for ind, consumer in enumerate(consumer_menu):
    for s in consumer:
        sushi_dict[s].append(ind+1)

counter = [0 for _ in range(N)]

for sushi in sushi_num:
    for ind, consumer in enumerate(consumer_menu):
        if sushi in consumer:
            consumer_menu[ind].remove(sushi)
            counter[ind] += 1
            break

print(" ".join(map(str, counter)))
