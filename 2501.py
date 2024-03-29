# https://www.acmicpc.net/problem/2501
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())

ans = set([])
for i in range(1, N+1):
    if N%i==0:
        ans.add(N//i)

ans = sorted(list(ans))
if len(ans) >= K:
    print(f"{list(ans)[K-1]}")
else:
    print("0")
