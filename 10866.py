# https://www.acmicpc.net/problem/10866
import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(f"{str(x)}\n")


class Deque:
    def __init__(self):
        self.data = []

    def push_front(self, x):
        self.data.insert(0, x)

    def push_back(self, x):
        self.data.append(x)

    def pop_front(self):
        if len(self.data) == 0:
            print(-1)
        else:
            print(self.data.pop(0))

    def pop_back(self):
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

    def front(self):
        if len(self.data)==0:
            print(-1)
        else:
            print(self.data[0])

    def back(self):
        if len(self.data)==0:
            print(-1)
        else:
            print(self.data[len(self.data)-1])

    def __call__(self, command):
        if command.startswith("push_front"):
            self.push_front(int(command.split(" ")[1]))
        elif command.startswith("push_back"):
            self.push_back(int(command.split(" ")[1]))
        elif command.startswith("pop_front"):
            self.pop_front()
        elif command.startswith("pop_back"):
            self.pop_back()
        elif command.startswith("size"):
            self.size()
        elif command.startswith("empty"):
            self.empty()
        elif command.startswith("front"):
            self.front()
        elif command.startswith("back"):
            self.back()
        else:
            return None


if __name__=="__main__":
    command_num = int(input())
    deque = Deque()
    for i in range(1, command_num+1):
        deque(input())