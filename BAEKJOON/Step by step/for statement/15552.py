import sys

input = sys.stdin.readline

case = int(input())
for i in range(case):
    A, B = map(int, input().split())
    print(A + B)