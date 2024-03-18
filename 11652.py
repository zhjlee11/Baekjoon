# https://www.acmicpc.net/problem/11652
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

counter = {k:0 for k in cards}
for card in cards:
    counter[card] += 1

max_count = 0
max_card = 0
for card, count in counter.items():
    if count > max_count:
        max_count = count
        max_card = card
    elif count == max_count:
        max_card = min(max_card, card)

print(f"{max_card}")