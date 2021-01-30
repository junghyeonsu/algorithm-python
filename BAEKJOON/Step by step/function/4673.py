def d(n):
    next = n
    for value in list(str(n)):
        next += int(value)
    return next


excep = []
for count in range(10001):
    excep.append(d(count))


for i in range(10001):
    if i in excep:
        continue
    else:
        print(i)