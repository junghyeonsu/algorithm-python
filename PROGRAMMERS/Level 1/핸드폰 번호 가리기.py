def solution(phone_number):
    answer = ""
    answer += phone_number[::-1][:4]
    for i in range(len(phone_number[::-1][4:])):
        answer += "*"
    return answer[::-1]