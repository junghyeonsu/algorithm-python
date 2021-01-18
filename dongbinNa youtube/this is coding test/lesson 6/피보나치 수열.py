# 지수 시간 복잡도를 가지게 된다.
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x - 1) + fibo(x - 2)

# print(fibo(99))


# DP를 이용한 피보나치
d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))
