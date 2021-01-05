list = input().split(' ')
h = int(list[0])
m = int(list[1])
if m < 45:
    if h == 0:
        h = 23
        m += 15
    else:
        h -= 1
        m += 15
else:
    m -= 45
print(h, m)