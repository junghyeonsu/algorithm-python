import heapq


def solution(N, stages):
    count = [0] * (N + 1)
    for stage in stages:
        count[stage - 1] += 1

    fail = []
    for i in range(len(count) - 1):
        people = 0
        for j in range(i, len(count)):
            people += count[j]
        if people == 0:
            heapq.heappush(fail, (0, i + 1))
            continue
        heapq.heappush(fail, (-(count[i] / people), i + 1))

    answer = []
    for i in range(len(fail)):
        answer.append(heapq.heappop(fail)[1])

    return answer