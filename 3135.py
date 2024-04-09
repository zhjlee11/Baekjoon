# https://www.acmicpc.net/problem/3135
import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

A, B = map(int, input().split())
N = int(input())
star_list = []
for _ in range(N):
    star_list.append(int(input()))

min_count = min([abs(B-A)] + [abs(B-s)+1 for s in star_list])
print(f"{str(min_count)}")