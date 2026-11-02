
def cost(board):
    count = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                count += 1
    return count


def hill_climbing(board):
    while cost(board) != 0:
        best = board[:]
        min_cost = cost(board)

        for col in range(4):
            for row in range(4):
                if row != board[col]:
                    temp = board[:]
                    temp[col] = row

                    if cost(temp) < min_cost:
                        best = temp
                        min_cost = cost(temp)

        if best == board:
            return None

        board = best

    return board


board = [0, 3, 0, 2]

print("Neighbor Costs:")
count = 0

for col in range(4):
    for row in range(4):
        if row != board[col]:
            temp = board[:]
            temp[col] = row
            print(temp, "=", cost(temp))
            count += 1

            if count == 6:
                break
    if count == 6:
        break

result = hill_climbing(board)

print("\nFinal Solution:", result)
if result:
    print("Final Cost:", cost(result))
