def solution(n, lost, reserve):
    new_lost = [l for l in lost if l not in reserve]
    new_reserve = [r for r in reserve if r not in lost]
    for i in new_reserve:
        if i - 1 in new_lost:
            new_lost.remove(i - 1)
        elif i + 1 in new_lost:
            new_lost.remove(i + 1)
    return n - len(new_lost)