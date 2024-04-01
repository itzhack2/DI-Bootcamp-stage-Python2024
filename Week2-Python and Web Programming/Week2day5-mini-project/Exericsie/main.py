def display_board(board):
    """Display the Tic Tac Toe board."""
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")


def player_input(player):
    """Get the position from the player."""
    position = input(f"Player {player}, enter your position (1-9): ")
    while not position.isdigit() or not (1 <= int(position) <= 9):
        position = input("Invalid input! Please enter a number between 1 and 9: ")
    return int(position)


def check_win(board):
    """Check whether there is a winner or not."""
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return True

    for col in range(3):
        if len(set(board[row][col] for row in range(3))) == 1 and board[0][col] != ' ':
            return True

    if len(set(board[i][i] for i in range(3))) == 1 and board[0][0] != ' ':
        return True

    if len(set(board[i][2 - i] for i in range(3))) == 1 and board[0][2] != ' ':
        return True

    return False


def play():
    """Main function to play the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    display_board(board)

    players = ['X', 'O']
    current_player = 0

    for _ in range(9):
        position = player_input(players[current_player])
        row, col = (position - 1) // 3, (position - 1) % 3

        while board[row][col] != ' ':
            print("Position already occupied! Please choose another position.")
            position = player_input(players[current_player])
            row, col = (position - 1) // 3, (position - 1) % 3

        board[row][col] = players[current_player]
        display_board(board)

        if check_win(board):
            print(f"Player {players[current_player]} wins!")
            return

        current_player = (current_player + 1) % 2

    print("It's a tie!")


if __name__ == "__main__":
    play()
