def manhattan(state, goal):
    distance = 0

    for tile in range(1, 9):
        current_pos = state.index(tile)
        goal_pos = goal.index(tile)

        current_row = current_pos // 3
        current_col = current_pos % 3

        goal_row = goal_pos // 3
        goal_col = goal_pos % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)

    # Move Up
    if zero >= 3:
        new_state = list(state)
        new_state[zero], new_state[zero - 3] = new_state[zero - 3], new_state[zero]
        neighbors.append(tuple(new_state))

    # Move Down
    if zero < 6:
        new_state = list(state)
        new_state[zero], new_state[zero + 3] = new_state[zero + 3], new_state[zero]
        neighbors.append(tuple(new_state))

    # Move Left
    if zero % 3 != 0:
        new_state = list(state)
        new_state[zero], new_state[zero - 1] = new_state[zero - 1], new_state[zero]
        neighbors.append(tuple(new_state))

    # Move Right
    if zero % 3 != 2:
        new_state = list(state)
        new_state[zero], new_state[zero + 1] = new_state[zero + 1], new_state[zero]
        neighbors.append(tuple(new_state))

    return neighbors


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def a_star(initial, goal):

    OPEN = [initial]
    CLOSED = set()

    g = {initial: 0}
    parent = {initial: None}

    while OPEN:

        # Select state with lowest f value
        current = min(
            OPEN,
            key=lambda state: g[state] + manhattan(state, goal)
        )

        h = manhattan(current, goal)
        f = g[current] + h

        print("Current State:")
        print_puzzle(current)

        print("g =", g[current], "h =", h, "f =", f)

        # Goal test
        if current == goal:
            print("Goal Reached!")

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            
            print("Total moves =", len(path) - 1)
            return

        OPEN.remove(current)
        CLOSED.add(current)

        # Generate successors
        for next_state in get_neighbors(current):

            if next_state in CLOSED:
                continue

            new_g = g[current] + 1

            if next_state not in OPEN or new_g < g.get(next_state, 999):

                g[next_state] = new_g
                parent[next_state] = current

                if next_state not in OPEN:
                    OPEN.append(next_state)

    print("No solution found!")


# -------------------------------
# INPUT
# -------------------------------

print("Enter Initial State")
print("Use 0 for blank space")

initial = tuple(map(int, input().split()))

print("Enter Goal State")

goal = tuple(map(int, input().split()))

print("\nInitial State:")
print_puzzle(initial)

print("Goal State:")
print_puzzle(goal)

a_star(initial, goal)