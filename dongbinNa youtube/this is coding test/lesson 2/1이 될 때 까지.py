def untilOne(num, k):
    count = 0
    while num != 1:
        if num % k != 0:
            num -= 1
            count += 1
        else:
            num /= k
            count += 1
    return count


print(untilOne(25, 3))