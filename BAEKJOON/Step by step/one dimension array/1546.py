import sys
input = sys.stdin.readline

n = int(input())
grade = list(map(int, input().split()))
top = max(grade)
new_grade = []
for i in grade:
    new_grade.append(round(i / top * 100, 1))


sum = 0
for i in new_grade:
    sum += i

print(sum/len(new_grade))