def solution(num):
    count = 0
    while num != 1:
        num = int(num / 2) if num % 2 == 0 else int(num * 3 + 1)
        count += 1
    return -1 if count >= 500 else count