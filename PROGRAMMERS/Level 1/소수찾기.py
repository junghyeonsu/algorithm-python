def solution(range_n):
    primes = []
    a = [False, False] + [True] * (range_n - 1)
    for i in range(2, range_n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, range_n + 1, i):
                a[j] = False
    return len(primes)