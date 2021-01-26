def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        item1 = bin(arr1[i]).lstrip("0b").zfill(n)
        item2 = bin(arr2[i]).lstrip("0b").zfill(n)
        print(item1, item2)
        temp = ""
        for j in range(n):
            if item1[j] == item2[j] and item1[j] == "1":
                temp += "#"
            elif item1[j] == "1" or item2[j] == "1":
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    return answer