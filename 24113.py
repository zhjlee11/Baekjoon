import sys
from copy import deepcopy

input = sys.stdin.readline
print = sys.stdout.write

arr1 = []
arr2 = []
arr_r = []

n1 = int(input())
for i in range(n1):
    arr1.append(list(map(int, input().split(" "))))
n2 = int(input())
for i in range(n2):
    arr2.append(list(map(int, input().split(" "))))

l1 = sum([c for _, c in arr1])
l2 = sum([c for _, c in arr2])
if l1>l2:
    arr2.append([0, l1-l2])
elif l1<l2:
    arr1.append([0, l2-l1])

while len(arr1)>0 or len(arr2)>0:
    a, c1 = arr1.pop(0)
    b, c2 = arr2.pop(0)

    if c1>c2:
        arr_r.append([a+b, c2])
        arr1.insert(0, [a, c1-c2])
    elif c1>c2:
        arr_r.append([a+b, c1])
        arr1.insert(0, [b, c2-c1])
