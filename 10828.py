# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(f"{str(x)}\n")


class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) == 0:
            print(-1)
        else:
            print(self.data.pop(len(self.data) - 1))

    def size(self):
        print(len(self.data))

    def empty(self):
        if len(self.data)==0:
            print(1)
        else:
            print(0)

    def top(self):
        if len(self.data)==0:
            print(-1)
        else:
            print(self.data[len(self.data)-1])

    def __call__(self, command):
        if command.startswith("push"):
            self.push(int(command.split(" ")[1]))
        elif command.startswith("pop"):
            self.pop()
        elif command.startswith("size"):
            self.size()
        elif command.startswith("empty"):
            self.empty()
        elif command.startswith("top"):
            self.top()
        else:
            return None


if __name__=="__main__":
    command_num = int(input())
    stack = Stack()
    for i in range(1, command_num+1):
        stack(input())