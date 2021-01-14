n = 4
m = 6
arr = [19, 15, 10, 17]

# 내가 푼 풀이
def made(arr, n, m):
    remain = 0
    min_m = []
    # 1 ~ arr의 최대값까지 돌면서
    for i in range(1, max(arr) + 1):
        # arr의 값을 하나씩 다돌면서
        for j in arr:
            # 남은 길이를 계산
            if j > i:
                remain += j % i
        if remain >= m:
            min_m.append(remain)
        else:
            min_m.append(sum(arr))
        remain = 0
    return max(arr) - min_m[::-1].index(min(min_m))


# 영상 풀이
def made2(arr, n, m):
    result = 0
    start = 0
    end = max(arr)
    while start <= end:
        remain = 0
        mid = (end + start) // 2

        for x in arr:
            if x > mid:
                remain += x - mid

        if remain < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)


made2(arr, n, m)