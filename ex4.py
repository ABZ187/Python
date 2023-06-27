# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

i = int(input())
dict = {}
j = []
for _ in range(i):
    b = sys.stdin.readline()
    list = b.split()
    dict[list[0]] = list[1]
for m in range(i):
    c = sys.stdin.readline().rstrip("\n")
    j.append(c)
for c in j:
    if c in dict:
        sys.stdout.write(f"{c}={dict[c]}\n")
    else:
        sys.stdout.write("Not found\n")
