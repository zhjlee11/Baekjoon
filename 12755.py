# https://www.acmicpc.net/problem/12755
import sys

input = sys.stdin.readline
print = lambda x : sys.stdout.write(f"{x}")

N = int(input())

for i in range(1, N+1):
    num_str = str(i)
    N -= len(num_str)

    if N <= 0:
        print(num_str[len(num_str)-1+N])
        break