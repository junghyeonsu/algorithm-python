def solution(s, n):
    a = "abcdefghijklmnopqrstuvwxyz"
    A = a.upper()
    answer = ""
    for i in s:
        if i == " ":
            answer += " "
        elif i.islower():
            num = a.find(i)
            answer += a[(num + n) % 26]
        else:
            num = A.find(i)
            answer += A[(num + n) % 26]
    return answer