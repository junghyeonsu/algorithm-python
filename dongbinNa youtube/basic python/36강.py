# 딕셔너리 자료형
# key : value 의 쌍의 값이 원소로 들어간다.

dict = {} # 중괄호가 사용된다.

# 특정한 key에 value를 넣는다
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'Effort'

# index, key값을 출력
for i, k in enumerate(dict):
    print(i)
    print(k, ' = ', dict[k])
    
# 삭제
del dict['기적']
# 모두 삭제
dict.clear() 
# 길이
len(dict)

# 키 값만 출력
keys = dict.keys()
# 그 다음 리스트로 변경
key_list = list(keys)


# value 값만 출력
values = dict.values()
values_list = list(values)

# 정렬
sorted(dict) # 오름차순 사전식 정렬
sorted(dict, reverse=True) # 내림차순
sorted(dict.values()) # 값만 오름차순