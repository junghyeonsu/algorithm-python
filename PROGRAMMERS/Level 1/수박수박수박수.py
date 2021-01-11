def solution(n):
    s1 = "수"
    s2 = "박"
    answer = ""
    count = 1
    for i in range(n):
        if count % 2 == 0:
            answer += s2
        else:
            answer += s1
        count += 1
    return answer