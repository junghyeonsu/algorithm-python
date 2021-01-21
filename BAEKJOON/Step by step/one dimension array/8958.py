import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    count = 0
    sum = 0
    string = input()
    for j in string:
        if j == 'O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)