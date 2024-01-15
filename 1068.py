# https://www.acmicpc.net/problem/1068
import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(f"{str(x)}\n")

class Tree:
    def __init__(self, node_num, parents_node):
        self.data = {}
        self.parents_node = {}

        for node in range(node_num):
            self.data[node] = []

        for child, parent in enumerate(parents_node):
            self.parents_node[child] = parent
            if parent!=-1:
                self.data[parent].append(child)
    def delete_node(self, x):
        child_nodes = self.data[x]
        parent = self.parents_node[x]
        if parent!=-1 and parent in self.data.keys():
            self.data[parent].remove(x)
        del self.data[x]
        for child in child_nodes:
            self.delete_node(child)

    def count_leaf(self):
        count = 0
        for child_nodes in self.data.values():
            count += (1 if len(child_nodes)==0 else 0)
        return count


if __name__=="__main__":
    node_num = int(input())
    parents_node = map(int, input().split(" "))
    tree = Tree(node_num, parents_node)
    tree.delete_node(int(input()))
    print(tree.count_leaf())