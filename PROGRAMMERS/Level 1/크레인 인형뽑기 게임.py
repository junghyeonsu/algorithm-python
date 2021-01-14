bucket = []


def solution(board, moves):
    bomb = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                bucket.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
        while len(bucket) >= 2:
            a = bucket.pop()
            b = bucket.pop()
            if a == b:
                bomb += 2
            else:
                bucket.append(b)
                bucket.append(a)
                break
    return bomb