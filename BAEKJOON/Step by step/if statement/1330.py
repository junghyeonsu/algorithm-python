list = input().split(' ')
a = int(list[0])
b = int(list[1])
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")