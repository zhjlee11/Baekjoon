# https://www.acmicpc.net/problem/15486
import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(f"{str(x)}\n")

if __name__=="__main__":
    N = int(input())
    dp = [0 for _ in range(N + 1)]
    data = {}

    for day in range(1, N+1):
        data[day] = list(map(int, input().split(" ")))
        for old_day in range(day):
            if data[old_day+1][0] <= day - old_day:
                new_v = dp[old_day] + data[old_day+1][1]
                if dp[day] < new_v:
                    dp[day] = new_v

    print(dp[N])