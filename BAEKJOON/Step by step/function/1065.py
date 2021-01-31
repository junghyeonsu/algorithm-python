# 한수
def ishansu(n):
    gap = []
    for i in range(len(n) - 1):
        gap.append(n[i] - n[i + 1])
    if gap[0] == gap[1]:
        return True
    else:
        return False


n = int(input())
count = 0
for i in range(1, n + 1):
    if len(str(i)) == 1 or len(str(i)) == 2:
        count += 1
    else:
        a = list(map(int, str(i)))
        if ishansu(a):
            count += 1
print(count)
