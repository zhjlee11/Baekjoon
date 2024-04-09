# https://www.acmicpc.net/problem/31090
import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for i in range(t):
    N = input()
    last = int(N[-3:])
    next = int(N)+1

    if next%last==0:
        print("Good\n")
    else:
        print("Bye\n")

