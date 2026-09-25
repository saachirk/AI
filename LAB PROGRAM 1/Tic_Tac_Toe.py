# Tic-Tac-Toe using Goal-Based Agent

board = [" "] * 9


def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):
            return True

    return False


def agent_move():

    # Goal 1: Win
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            if check_winner("X"):
                return

            board[i] = " "

    # Goal 2: Block opponent
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            if check_winner("O"):
                board[i] = "X"
                return

            board[i] = " "

    # Goal 3: Take center
    if board[4] == " ":
        board[4] = "X"
        return

    # Goal 4: Take a corner
    corners = [0, 2, 6, 8]

    for i in corners:
        if board[i] == " ":
            board[i] = "X"
            return

    # Goal 5: Take any empty position
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            return


def play_game():

    while True:

        display_board()

        # Human move
        move = int(input("Enter position (1-9): ")) - 1

        if board[move] != " ":
            print("Position already occupied!")
            continue

        board[move] = "O"

        if check_winner("O"):
            display_board()
            print("Human Wins!")
            break

        if " " not in board:
            display_board()
            print("Draw!")
            break

        # AI move
        agent_move()

        if check_winner("X"):
            display_board()
            print("AI Wins!")
            break

        if " " not in board:
            display_board()
            print("Draw!")
            break


# Start the game
play_game()