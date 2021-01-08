def solution(s):
    length = len(s)
    if length % 2 == 0: # 짝수 개
        start = int(length / 2)
        answer = s[start-1] + s[start]
    else:               # 홀수 개
        start = int(length / 2)
        answer = s[start]
    return answer