# 여행을 떠날 수 있는 그룹 수의 최댓값을 출력
# 최대로 보내려면 작은 수 그룹부터 먼저 보내야한다는 아이디어
def func(n, fear):
    fear = sorted(fear)
    count = 0
    group = 0
    for i in fear:
        count += 1
        if count >= i:
            group += 1
            count = 0
    print(group)            


func(5, [2,3,1,2,2])