
with open('input.txt', 'r') as f:
    numbers = f.readline().split(",")

    boards = []
    current_board = []
    for line in f.readlines():
        if line.strip() != "":
            current_board.append(line.strip().split())
        elif len(current_board) > 0:
            boards.append(current_board)
            current_board = []
    if len(current_board) == 5:
        boards.append(current_board)
    else:
        print(len(current_board))
        print("ERROR BAD!!!")

def board_won(board, picked_numbers):
    for i in range(0, 5):
        row_won = True
        column_won = True
        diagonal_a_won = True
        diagonal_b_won = True
        for j in range(0, 5):
            if not board[i][j] in picked_numbers:
                row_won = False
            if not board[j][i] in picked_numbers:
                column_won = False
            if not board[i][i] in picked_numbers:
                diagonal_a_won = False
            if not board[i][4-i] in picked_numbers:
                diagonal_b_won = False
        if row_won or column_won:  # or diagonal_a_won or diagonal_b_won:
            return board

    return None

def find_score(board, index, picked_numbers):
    sum = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] not in picked_numbers:
                sum += int(board[i][j])

    return sum * int(picked_numbers[index - 1])

print(numbers)
print(boards)

picked_numbers = []
winning_board = None
for i in range(1, len(numbers)):
    for board in boards:
        winning_board = board_won(board, numbers[0:i])
        if winning_board is not None:
            break

    if winning_board is not None:
        break

print(winning_board)
print(numbers[0:i])
print(find_score(winning_board, i, numbers[0:i]))