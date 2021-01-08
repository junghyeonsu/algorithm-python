def solution(s):
    lower = []
    upper = []
    answer = ""
    for i in s:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    
    lower = sorted(lower, reverse=True)
    upper = sorted(upper, reverse=True)

    for i in lower:
        answer += i
    for i in upper:
        answer += i
    
    print(answer)
    
    return answer