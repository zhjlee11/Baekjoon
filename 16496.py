# https://www.acmicpc.net/problem/16496
from copy import deepcopy
import sys
input = sys.stdin.readline
print = sys.stdout.write

total_components = []
greed_list = []

def compare(a, b):
    if a==b:
        return None
    return int(str(a)+str(b)) > int(str(b)+str(a))

def getGreedList(components):
    greed_list = [0 for _ in range(len(components))]

    for i, a in enumerate(components):
        for j, b in enumerate(components):
            if i!=j:
                comp = compare(a, b)
                if comp == False:
                    greed_list[j] += 1

    return greed_list

def search(components, greed_list, number=""):
    if len(components) == 0:
        return number
    cp_list = deepcopy(components)
    g_list = deepcopy(greed_list)
    max_ind = 0
    max_greed = deepcopy(g_list[0])
    for i, greed in enumerate(g_list):
        if greed > max_greed:
            max_ind = i
            max_greed = deepcopy(greed)
    number += str(cp_list[max_ind])
    del cp_list[max_ind], g_list[max_ind]
    return search(cp_list, g_list, number)



if __name__=="__main__":
    input()
    total_components = list(map(int, input().split(" ")))
    greed_list = getGreedList(total_components)

    #print(f"{str(greed_list)}\n")
    #print(f"{str(total_components)}\n")

    result = search(total_components, greed_list)
    result = result if result != "" else "0"
    print(f"{str(int(result))}")