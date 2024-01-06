import sys
input = sys.stdin.readline
print = sys.stdout.write

def encode(n):
    num_str = ''

    for i in range(n):
        k = list(map(int, input().split(" ")))
        num_str += str(k[0]) * int(k[1])

    return int(num_str)

def decode(n):
    lastchar = str(n)[0]
    num = 1

    result=[]
    for char in str(n)[1:]:
        if char==lastchar:
            num += 1
        else :
            result.append(f"{lastchar} {num}\n")
            lastchar = char
            num = 1
    result.append(f"{lastchar} {num}\n")

    print(f"{len(result)}\n")
    for stri in result:
        print(stri)

num1 = encode(int(input()))
num2 = encode(int(input()))
decode(num1+num2)