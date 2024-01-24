# https://www.acmicpc.net/problem/11726
import sys
input = sys.stdin.readline
print = sys.stdout.write

if __name__=="__main__":
    n = int(input())
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    if n>=2:
        dp[2] = 2

    if n>=3:
        for i in range(3, n+1):
            dp[i] = (dp[i - 1] + dp[i - 2])%10007

    print(f"{str(dp[n])}")