# https://www.acmicpc.net/problem/30402
import sys
input = sys.stdin.readline
print = sys.stdout.write

image = [[*input().split()] for _ in range(15)]
for row in image:
    if 'w' in row:
        print("chunbae")
        break
    elif 'b' in row:
        print("nabi")
        break
    elif 'g' in row:
        print("yeongcheol")
        break