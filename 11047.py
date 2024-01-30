# https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(f"{str(x)}")

if __name__=="__main__":
    N, K = map(int, input().split(" "))
    A = []
    for _ in range(N):
        A.append(int(input()))
    A.sort(reverse=True)

    num = 0
    while K>0:
        for coin in A:
            if K//coin >= 1:
                num += K//coin
                K = K%coin
                A.remove(coin)
                break

    print(num)