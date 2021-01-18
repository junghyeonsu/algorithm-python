n, m = input().split()
worthy = []
for i in range(int(n)):
    k = int(input())
    worthy.append(k)

d = [10001] * (int(m) + 1)
d[0] = 0

for i in range(1, len(d)):
    for k in worthy:
        if i - k < 0:
            continue
        elif d[i - k] != 10001:
            d[i] = min(d[i], d[i - k] + 1)


if d[int(m)] == 10001:
    print(-1)
else:
    print(d[int(m)]) 