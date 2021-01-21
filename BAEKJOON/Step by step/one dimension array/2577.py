import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
num = list(map(int, str(a * b * c)))
result = [0] * 10

for i in num:
    result[i] += 1

for i in result:
    print(i)