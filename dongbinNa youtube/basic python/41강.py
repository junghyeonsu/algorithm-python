# 람다식은 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법
add = lambda x, y: x + y
print(add(1, 2))


# map() : 다수의 원소에 대한 함수의 결과를 한 번에 얻을 수 있도록 도와준다
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
my_function = lambda a, b : a + b
# list1과 list2 각 원소에 my_function을 적용해서 새로운 리스트로 반환한다.
map_list = map(my_function, list1, list2)
print(list(map_list))

