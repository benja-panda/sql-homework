def init_board():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def get_move(board, mark):
    moves_map = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }

    while True:
        user_input = input(f"תור שחקן {mark} - בחר משבצת (1-9): ").strip()

        if not user_input.isdigit():
            print("שגיאה: יש להזין מספר בלבד! נסה שוב.")
            continue

        square = int(user_input)

        if square not in moves_map:
            print("שגיאה: המספר חייב להיות בין 1 ל-9! נסה שוב.")
            continue

        row, col = moves_map[square]

        if board[row][col] != ' ':
            print("שגיאה: משבצת זו כבר תפוסה! בחר משבצת אחרת.")
            continue

        return row, col


def check_winner(board, mark):
    for row in board:
        if row[0] == row[1] == row[2] == mark:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True

    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True

    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def ask_play_again():
    while True:
        choice = input("\nהאם תרצו לשחק סיבוב נוסף? (כן/לא): ").strip().lower()
        if choice in ['כן', 'y', 'yes']:
            return True
        elif choice in ['לא', 'n', 'no']:
            return False
        else:
            print("תשובה לא תקינה, אנא הקלד 'כן' או 'לא'.")


def play_round():
    board = init_board()
    print_board(board)

    while True:
        # תור X
        row, col = get_move(board, "X")
        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("🎉 כל הכבוד! שחקן X ניצח!")
            break

        if is_board_full(board):
            print("🤝 המשחק הסתיים בתיקו!")
            break

        # תור O
        row, col = get_move(board, "O")
        board[row][col] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("🎉 כל הכבוד! שחקן O ניצח!")
            break


def main():
    print("=== ברוכים הבאים למשחק איקס עיגול! ===")

    while True:
        play_round()
        if not ask_play_again():
            print("\nתודה ששיחקתם! להתראות 👋")
            break


if __name__ == "__main__":
    main()