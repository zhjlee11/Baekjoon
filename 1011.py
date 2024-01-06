import sys
input = sys.stdin.readline
print = sys.stdout.write

def count_min_num(x, y):
    d = y-x
    a = int(d**0.5)
    r = d - a**2
    weights = [0]*a

    for i in range(a, 0, -1):
        weights[i-1] = r//i
        r = r%i

    return 2*a-1 + sum(weights)

try_num = int(input())
result = []
for i in range(try_num):
    x, y = list(map(int, input().split(" ")))
    result.append(count_min_num(x, y))

for i, val in enumerate(result):
    print(f"{val}")
    if i != try_num-1 :
        print("\n")