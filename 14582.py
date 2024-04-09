# https://www.acmicpc.net/problem/14582
import sys
input = sys.stdin.readline
print = sys.stdout.write

g_win = list(map(int, input().split()))
s_win = list(map(int, input().split()))

g_sum, s_sum = 0, 0
result = "No"
for g, s in zip(g_win, s_win):
    g_sum += g
    s_sum += s

    if g_sum > s_sum-s :
        result = "Yes"
        break

print(result)