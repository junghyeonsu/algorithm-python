import sys

input = sys.stdin.readline

c = int(input())
for i in range(c):
    students = list(map(int, input().split()))
    count = 0
    add = sum(students) - students[0]
    mean = add / students[0]
    for j in range(1, len(students)):
        if students[j] > mean:
            count += 1
    print("%.3f%%" % (count / (len(students) - 1) * 100))