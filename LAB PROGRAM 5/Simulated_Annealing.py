
import random
import math

def cost(board):
    count = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                count += 1
    return count


def simulated_annealing():
    while True:
        board = [random.randint(0, 7) for _ in range(8)]
        T = 100

        while T > 0.001:
            current = cost(board)

            if current == 0:
                return board

            temp = board[:]
            col = random.randint(0, 7)
            temp[col] = random.randint(0, 7)

            delta = cost(temp) - current

            if delta < 0 or random.random() < math.exp(-delta / T):
                board = temp

            T *= 0.99


result = simulated_annealing()

print("Final Solution:", result)
print("Cost:", cost(result))
print("Goal State Reached!")
