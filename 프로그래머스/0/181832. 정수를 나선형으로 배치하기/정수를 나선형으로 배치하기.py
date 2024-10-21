def move(x, y, mode):
    if mode == 0:
        return x + 1, y
    if mode == 1:
        return x, y + 1
    if mode == 2:
        return x - 1, y
    if mode == 3:
        return x, y - 1


def mode_change(x, y, board, mode):
    a, b = move(x, y, mode)
    if a < 0 or a == len(board) or b < 0 or b == len(board) or board[b][a] != 0:
        mode += 1
        mode %= 4
    return mode


def solution(n):
    answer = []
    for i in range(n):
        t = []
        for k in range(n):
            t.append(0)
        answer.append(t)
    x = 0
    y = 0
    mode = 0
    i = 1
    while i <= n ** 2:
        answer[y][x] = i
        mode = mode_change(x, y, answer, mode)
        x, y = move(x, y, mode)
        i += 1
    return answer