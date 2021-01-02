# 실수 + 정수 = 실수
# 문자열 + 실수(정수) = 오류
a = 9
b = 7
print("a + b : ", a + b)
print("a - b : ", a - b)
print("a * b : ", a * b)
print("a / b : ", a / b) # 소수점까지 계산을 해준다.
print("a // b : ", a // b) # 몫만 얻고싶을 때
print("a % b : ", a % b)

# 복소수 계산도 해준다.
a = (1 + 2j)
b = (3 + 4j)
print(a * b)