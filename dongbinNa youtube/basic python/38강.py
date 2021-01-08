# 문자열 자료형 뒤집기 : 슬라이싱 활용
str = 'Hello World'
# print(str[::-1])

# len() : 문자열 길이 활용
# print(len(str))

# isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인
str = "HelloWorld"
print(str.isalpha()) # 공백도 문자열로 안 침

# isdigit() : 숫자로만 이루어져 있나?
num = "12"
print(num.isdigit())

# isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
str = 'abc123'
print(str.isalnum)

# join(리스트 자료형) : 여러 개의 문자열을 구분자와 함께 합치는 함수
list = ['Hello', 'World', '홍길동']
print('->'.join(list))

# sorted(문자열 자료형) : 각 문자를 정렬하는 함수
str = 'helloworld'
list = sorted(str, reverse=True)
print(list) # 오름차순으로 리스트로 정렬해서 담아줌
print(''.join(list))

# split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
str = 'I wanna watch a movie.'
list = str.split(' ')
print(list)

# find(문자열) : 토큰의 위치를 인덱스로 알려준다.
# 문자열이 포함되어있지 않으면 -1 을 반환
# 두번 째 매개변수는 몇 번째 인덱스 이후에 문자열을 찾겠다하고 넣어줄수있음

# strip() : 좌우로 특정한 문자열을 제거하는 함수
str = ' Hello World '
print(str.strip())
# 왼쪽 공백만 제거 = lstrip()
# 오른쪽 공백 제거 = rstrip()
# strip안에 매개변수를 넣으면 그 문자만 없어짐

# eval() : 문자열 수식 계산을 해주는 함수
exp = "(203+705)*3"
print(eval(exp))