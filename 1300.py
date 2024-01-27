import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(f"{str(x)}\n")

def scalar_product(scalr, array):
    return [scalr*element for element in array]

def flatten(matrix):
    result = []
    for array in matrix:
        result += array
    return result

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    meaningful_n = n
    for i in range(1, n+1):
        if i**2>k:
            meaningful_n = i