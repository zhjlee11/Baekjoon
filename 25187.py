# https://www.acmicpc.net/problem/25187
import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(f"{str(x)}\n")

tanks = {}
parents = {}

def find_parent(x):
    global parents
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(a, b):
    global parents
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def exportToSet(parents, tanks):
    set_list = {}
    for child, parent in parents.items():
        if child==parent:
            set_list[child] = {child}

    for child, parent in parents.items():
        if child!=parent:
            root = find_parent(child)
            set_list[root].add(child)
    set_list = list(set_list.values())

    set_by_clean = []
    for s in set_list:
        count_cleanWater = 0
        count_fixedWater = 0
        for ele in s:
            if tanks[ele]:
                count_cleanWater += 1
            else:
                count_fixedWater += 1
        if count_cleanWater > count_fixedWater:
            set_by_clean.append([list(s), True])
        else:
            set_by_clean.append([list(s), False])

    result = {}
    for s, isClean in set_by_clean:
        for ele in s:
            result[ele] = isClean

    return result




if __name__ == "__main__":
    n, m, q = map(int, input().split(" "))

    tank_inp = map(int, input().split(" "))
    tanks = {ind+1:isClean==1 for ind, isClean in enumerate(tank_inp)}

    parents = {i:i for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split(" "))
        union_parent(u, v)

    result = exportToSet(parents, tanks)

    answer = []
    for _ in range(q):
        k = int(input())
        answer.append(result[k])

    for output in answer:
        print(1 if output else 0)