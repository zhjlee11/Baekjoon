# https://www.acmicpc.net/problem/2839
import sys
input = sys.stdin.readline
print = sys.stdout.write

if __name__ == "__main__":
    n = int(input())

    num_5gk = n // 5
    num_3kg = 0

    result = -1
    while num_5gk >= 0 :
        if (n-5*num_5gk)%3==0:
            num_3kg = (n-5*num_5gk)//3
            result = num_5gk+num_3kg
            break
        else:
            num_5gk -= 1

    print(f"{str(result)}")
