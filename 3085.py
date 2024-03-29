# https://www.acmicpc.net/problem/3085
import sys

input = sys.stdin.readline
print = sys.stdout.write


def transpose(board, n):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            result[x][y] = board[y][x]
    return result


def step(target, N):
    global color_counter

    max_num = 0
    for line in target:
        for color in color_counter.keys():
            checker = [False for _ in range(N)]
            for ind, pos in enumerate(line):
                if pos == color:
                    checker[ind] = True

            if False not in checker:
                return N
            elif checker.count(False) == 1 and color_counter[color] >= N:
                return N
            elif True not in checker:
                continue
            else:
                for checker_l in (checker, list(reversed(checker))):
                    cnt = 1
                    flag = True
                    start = checker_l.index(True)
                    for i in range(start + 1, len(checker_l)):
                        if checker_l[i]:
                            cnt += 1
                        else:
                            if flag:
                                flag = False
                                cnt += 1
                            else:
                                break
                    max_num = max(max_num, cnt)

    return max_num


color_counter = {"C": 0, "P": 0, "Z": 0, "Y": 0}

N = int(input())
board = []
for _ in range(N):
    board.append(list(input().replace("\n", "")))

for row in board:
    for color in row:
        color_counter[color] += 1

target = board + transpose(board, N)
answer = step(target, N)

print(str(answer))
