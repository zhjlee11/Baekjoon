import sys
input = sys.stdin.readline
print = sys.stdout.write

def count_zero_and_one(n):
    num_zero = [1, 0]
    if n==0:
        return f"{num_zero[n]} {num_zero[n+1]}"
    else:
        if n>1:
            for i in range(2, n+1):
                num_zero.append(num_zero[i-1] + num_zero[i-2])
        return f"{num_zero[n]} {num_zero[n]+num_zero[n-1]}"

run_time = int(input())
str = ""
for i in range(run_time):
    str += count_zero_and_one(int(input()))
    if i != run_time-1:
        str += "\n"

print(str)
