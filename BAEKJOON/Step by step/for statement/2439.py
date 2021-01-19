N = int(input())
count = N - 1
for i in range(1, N + 1):
    string = (" " * count) + ("*" * i)
    count -= 1
    print(string)