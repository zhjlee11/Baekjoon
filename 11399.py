# https://www.acmicpc.net/problem/11399
import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(f"{str(x)}")

if __name__=="__main__":
    N = int(input())
    dur_by_person = list(map(int, input().split(" ")))

    dur_by_person.sort()

    result = 0
    for ind, dur in enumerate(dur_by_person):
        result += (len(dur_by_person)-ind) * dur
    print(result)