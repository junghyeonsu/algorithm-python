t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    print("k : ", k)
    d = [0] * len(k)
    for j in range(m):
        for z in range(n):
            idx = j + (4 * z)
            print(idx, end=" ")
            # 첫번째 column
            if idx % m == 0:
                d[idx] = k[idx]
                print("첫번째 : ", d)
            # 맨 위에 row
            elif idx < m:
                d[idx] = max(d[idx - 1] + k[idx], d[idx + (m - 1)] + k[idx])
                print("두번째 : ", d)
            # 맨 아래 row
            elif idx > len(k) - m:
                d[idx] = max(d[idx - 1] + k[idx], d[idx - m - 1] + k[idx])
                print("세번째 : ", d)
            else:
                d[idx] = max(
                    d[idx - 1] + k[idx],
                    d[idx + (m - 1)] + k[idx],
                    d[idx - m - 1] + k[idx],
                )
                print("마지막번째 : ", d)

    answer = []
    for b in range(n):
        answer.append(d[(m - 1) + m * b])
    print("정답 : ", max(answer))
    print("배열 : ", d)