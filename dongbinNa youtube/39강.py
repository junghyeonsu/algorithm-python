# index(원소) : 리스트 내 특정한 원소 인덱스 찾기
'''
list = ['정현수', '김충환', '이지원', '백종현', '강명규', '김서경', '정준희']
print(list.index('정현수'))
'''
# 존재하지 않으면 오류가 뜸


# reverse() : 리스트의 원소를 뒤집는다.
'''
list.reverse()
print(list)
# or
print(list[::-1])
'''


# sum(리스트 자료형): 리스트의 모든 원소의 합
'''
list = [1,2,3]
print(sum(list))
'''
# 문자열 자료형과 숫자형 자료형은 함께 sum이 안됨


#range(): 특정 범위를 지정
'''
my_range = range(5, 10)
a = list(my_range)
print(list)
'''


# all() / any() : 리스트의 모든 함수가 참인지 / 하나라도 참인지
'''
list = [True, False, True]
print(all(list))
print(any(list))
'''


# enumerate() : 리스트에서 인덱스와 원소를 함께 추출
my_list = ['종', '서', '명', '준', '충', '지', '현']
result = list(enumerate(my_list))
print(result)


for i, k in enumerate(my_list):
    print(i , k)



# sort() : 리스트의 원소를 정렬
my_list = [1, 3, 5, 3, 4, 6, 1, 3]
my_list.sort()
print(my_list)


# count() : 특정한 원소의 개수를 추출

# del() : 리스트의 특정 원소를 제거

# insert(a, b) : a 해당 인덱스에 b의 값을 넣을 수 있음
# 또는 마지막에 넣고 싶으면 .append() 함수 사용