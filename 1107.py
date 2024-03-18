# https://www.acmicpc.net/problem/1107
import sys

input = sys.stdin.readline
print = sys.stdout.write

valid_button = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

N = int(input())
broken_button_num = int(input())
broken_buttons = map(int, input().split())
for button in broken_buttons:
    valid_button.remove(button)

nonzero_min = valid_button[1] if valid_button[0] == 0 else valid_button[0]
highest_num = int(str(N)[0])

min_distance_initial_channel = 100
for valid_num in valid_button:
    initial_channel = 100

    if valid_num < highest_num:
        pass
    elif valid_num == highest_num:
        pass
    else:
        if highest_num == 9:
            initial_channel = int(str(nonzero_min) + str(min(valid_button)) * len(str(N)))
        else:
            initial_channel = int(str(valid_num) + str(min(valid_button)) * (len(str(N)) - 1))

answer = min(abs(N-100), abs(N-min_distance_initial_channel)+len(str(min_distance_initial_channel)))
print(f"{answer}")