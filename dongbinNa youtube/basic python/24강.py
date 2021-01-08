# 리스트 : 비슷한 성질을 가진 객체의 나열
grade = [3.5, 3.6, 4.2, 4.3]

sum = 0
for i in grade:
    sum = sum + i

print("평균 점수 : ", sum/len(grade))