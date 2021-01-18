# 내 풀이
n = input()
n = int(n)
k = list(map(int, input().split()))
a = [0] * n
for i in range(len(k)):
    if i == 0:
        a[i] = k[i]
    elif i == 1:
        if k[i] > k[i - 1]:
            a[i] = k[i]
        else:
            a[i] = k[i-1]
    else:
        if a[i-1] > k[i] + a[i-2]:
            a[i] = a[i-1]
        else:
            a[i] = k[i] + a[i-2]

print(a[n-1])
    
# 동빈좌 풀이
n = int(input())
array = list(map(int, input().split()))
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])