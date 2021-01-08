# 0을 제외한 모든 수들은 곱셈을 하는 것이 수를
# 크게하는데 도움이 된다.
def test(input):
    answer = int(input[0])
    for i in range(1, len(input)):
        second = int(input[i])
        if answer == 0 or answer == 1 or second == 0 or second == 1:
            answer += second
        else:
            answer *= second
    return answer


print(test("02984"))