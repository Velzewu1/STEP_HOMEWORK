"""
2_task
"""
def print_board(field):
    """
    Creates a board
    """
    for line in field:
        print("|".join(line))
        print("-" * 5)

def check_winner(field, player):
    """
    Determines the winner
    """
    # Check rows and columns
    for i in range(3):
        if (all(field[i][j] == player for j in range(3)) or
            all(field[j][i] == player for j in range(3))):
            return True

    # Check diagonals
    if (all(field[i][i] == player for i in range(3)) or 
        all(field[i][2 - i] == player for i in range(3))):
        return True

    return False

def is_board_full(field):
    """
    Determines whether the board is full
    """
    return all(cell.isdigit() is False for row in field for cell in row)

if __name__ == "__main__":
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    CURRENT_PLAYER = "X"

    while True:
        print_board(board)

        try:
            move = int(input(f"Игрок {CURRENT_PLAYER}, введите номер ячейки (1-9): "))
            if 1 <= move <= 9:
                row, col = divmod(move - 1, 3)

                if board[row][col].isdigit():
                    board[row][col] = CURRENT_PLAYER

                    if check_winner(board, CURRENT_PLAYER):
                        print_board(board)
                        print(f"Игрок {CURRENT_PLAYER} победил!")
                        break
                    elif is_board_full(board):
                        print_board(board)
                        print("Ничья!")
                        break

                    CURRENT_PLAYER = "O" if CURRENT_PLAYER == "X" else "X"
                else:
                    print("Ячейка уже занята. Попробуйте еще раз.")
            else:
                print("Введите число от 1 до 9.")
        except ValueError:
            print("Введите число от 1 до 9.")
