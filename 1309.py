# https://www.acmicpc.net/problem/1309
import sys
input = sys.stdin.readline
print = sys.stdout.write

if __name__ == "__main__":
    n = int(input())
    dp = [1, 3] + [0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1] * 2) % 9901
    print(f"{str(dp[n])}")