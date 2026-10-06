# Tic-Tac-Toe CLI
# بازی دوز در محیط خط فرمان

board = [" " for _ in range(9)]


def show_board():
    """نمایش صفحه بازی"""

    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def show_positions():
    """نمایش شماره خانه‌ها"""

    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def check_winner(player):
    """بررسی برنده شدن بازیکن"""

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True

    return False


def is_draw():
    """بررسی مساوی شدن بازی"""

    return " " not in board


def play_game():
    """اجرای یک بازی"""

    global board

    board = [" " for _ in range(9)]

    current_player = "X"

    print("\n🎮 بازی دوز")
    print("بازیکن اول: X")
    print("بازیکن دوم: O")

    show_positions()

    while True:

        show_board()

        print(f"نوبت بازیکن {current_player}")

        try:
            position = int(input("شماره خانه را وارد کنید (1-9): "))

        except ValueError:
            print("❌ لطفاً فقط عدد وارد کنید.")
            continue

        if position < 1 or position > 9:
            print("❌ شماره خانه باید بین 1 تا 9 باشد.")
            continue

        index = position - 1

        if board[index] != " ":
            print("❌ این خانه قبلاً انتخاب شده است.")
            continue

        board[index] = current_player

        # بررسی برنده
        if check_winner(current_player):
            show_board()
            print(f"🎉 بازیکن {current_player} برنده شد!")
            break

        # بررسی مساوی
        if is_draw():
            show_board()
            print("🤝 بازی مساوی شد!")
            break

        # تغییر بازیکن
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def main():
    """تابع اصلی برنامه"""

    while True:

        play_game()

        again = input("\nآیا می‌خواهید دوباره بازی کنید؟ (y/n): ")

        if again.lower() != "y":
            print("\n👋 خداحافظ!")
            break


if __name__ == "__main__":
    main()
