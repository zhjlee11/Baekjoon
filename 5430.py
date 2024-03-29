# https://www.acmicpc.net/problem/5430
from collections import deque
import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x))

class AC:
    def __init__(self, len: int, array: list):
        self.len = len
        self.data = deque(array)

        self.is_R = False

    def __len__(self):
        return self.len

    def __str__(self):
        if self.is_R:
            self.data.reverse()
        return f"[{','.join(map(str, self.data))}]"

    def R(self):
        self.is_R = not self.is_R
        return True

    def D(self):
        if self.len >= 1:
            if self.is_R:
                self.data.pop()
            else:
                self.data.popleft()
            self.len-=1
            return True
        else:
            return False

    def __call__(self, command):
        if command=="R":
            return self.R()
        elif command=="D":
            return self.D()

result = ""
try_num = int(input())
for t in range(1, try_num+1):
    commands = list(input())
    ac = AC(int(input()), eval(input()))
    flag = False

    for command in commands:
        if ac(command) == False:
            result += "error\n"
            flag = True
            break
    if not flag:
        result += f"{str(ac)}\n"

print(result)