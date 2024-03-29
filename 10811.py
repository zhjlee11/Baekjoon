# https://www.acmicpc.net/problem/10811
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
method_list = []
for _ in range(M):
    method_list.append(list(map(int, input().split())))

bucket_list = list(range(1, N+1))
for method in method_list:
    start_ind = method[0]-1
    end_ind = method[1]-1

    bucket_list[start_ind:end_ind+1] = reversed(bucket_list[start_ind:end_ind+1])

print(" ".join(map(str, bucket_list)))