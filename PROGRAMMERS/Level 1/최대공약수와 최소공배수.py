def solution(n, m):
    answer = []
    if n >= m:
        X = gcd(n, m)
    else:
        X = gcd(m, n)
    answer.append(X)
    answer.append((n * m) // X)
    return answer


def gcd(X, Y):
    while Y:
        X, Y = Y, X % Y
    return X