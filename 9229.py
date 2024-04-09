# https://www.acmicpc.net/problem/9229
import heapq
import sys

input = sys.stdin.readline


# print = sys.stdout.write

def isWordGame(w1, w2):
    if len(w1) == len(w2):
        equal_list = [False for _ in range(len(w1))]
        for i in range(len(w1)):
            equal_list[i] = (w1[i] == w2[i])
        return equal_list.count(False) == 1
    return False


input_list = []
word = []
while True:
    line = input().replace("\n", "")
    if "#" in line and len(word) == 0:
        break
    elif "#" in line and len(word) > 0:
        input_list.append(word[:])
        word.clear()
    else:
        word.append(line)

output_list = []
for words in input_list:
    result = True

    for ind in range(len(words) - 1):
        result = isWordGame(words[ind], words[ind + 1]) and result

    output_list.append("Correct" if result else "Incorrect")

print("\n".join(output_list))
