# 숫자 범위 표현 : range(start, end)

# 1부터 10까지 반복이니까 10번
'''
for i in range(1, 10):
    print(i)
'''

# 5번 반복
'''
for i in range(5):
    print(i)
'''

# 문자열을 for 문에 넣어보기
'''
count = 0
for i in "Hello World":
    print(i)
    count = count + 1
'''

# print(count) # 이런식으로 문자열의 인덱스를 하나하나 방문해서 몇 개 인지 파악가능

# 리스트 처리
'''
sum = 0
list = [1,3,5,7,9]
for i in list:
    sum = sum + i

print(sum)
'''

# continue = continue를 만났을 때 더이상 수행하지 않고 다음 반복문을 수행
# break = break를 만났을 때 반복문을 나간다
# 짝수만 처리하는 for 문
'''
list = [1,2,3,4,5,6,7,8,9]
for i in list:
    # 홀수일 때는 continue를 만나서 없어짐
    if i % 2 == 1:
        continue
    print(i)
'''


# while (조건을 만족할 때 안의 내용을 반복)
'''
i = 0
sum = 0
while i < 5:
    i = i + 1
    if i % 2 == 1:
        continue
    sum = sum + i
print('합계 : ', sum)
'''