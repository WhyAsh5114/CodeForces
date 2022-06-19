for _ in range(int(input())):
    input()
    board = []
    for i in range(8):
        board.append(list(input()))
    
    active = False
    for i in range(8):
        if board[i].count('#') == 2:
            active = True
        if board[i].count('#') == 1 and active:
            col = i + 1
            row = board[i].index('#') + 1
            print(col, row)
            break