import sys

input = sys.stdin.readline
print = sys.stdout.write

def step(domain, length, previous_series=[]):
    global result
    if len(previous_series) == length:
        result.append(map(str, previous_series[:]))
    else:
        for ele in domain:
            next_domain = domain[:]
            next_domain.remove(ele)
            next_series = previous_series[:]
            next_series.append(ele)
            step(next_domain, length, previous_series=next_series)


result = []
n, m = map(int, input().split(" "))
domain = list(range(1, n + 1))
step(domain, m)
for per in result:
    print(f"{' '.join(per)}\n")
