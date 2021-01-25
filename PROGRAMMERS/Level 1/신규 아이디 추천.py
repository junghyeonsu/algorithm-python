def solution(new_id):
    # 1단계
    result = ""
    result = new_id.lower()

    # 2단계
    new_id = result
    result = ""
    possible = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "-",
        "_",
        ".",
    ]
    for i in range(len(new_id)):
        if new_id[i] in possible:
            result += new_id[i]

    # 3단계
    new_id = result
    result = []
    result.append(new_id[0])
    for i in range(1, len(new_id)):
        top = result[::-1][0]
        if top == new_id[i] and top == ".":
            pass
        else:
            result.append(new_id[i])

    result = "".join(result)

    # 4단계
    new_id = result
    result = ""
    result = new_id.strip(".")

    # 5단계
    new_id = result

    if len(new_id) == 0:
        result = ""
        result += "a"

    # 6단계
    new_id = result
    if len(new_id) >= 16:
        result = ""
        result = new_id[0:15]
        result = result.strip(".")

    # 7단계
    new_id = result
    if len(new_id) < 3:
        result = new_id
        last = new_id[::-1][0]
        while len(result) < 3:
            result += last

    return result