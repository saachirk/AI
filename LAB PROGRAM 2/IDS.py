def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def ACTIONS(state):
    actions = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    if row > 0:
        actions.append("UP")

    if row < 2:
        actions.append("DOWN")

    if col > 0:
        actions.append("LEFT")

    if col < 2:
        actions.append("RIGHT")

    return actions


def RESULT(state, action):
    state = list(state)
    blank = state.index(0)

    if action == "UP":
        new_blank = blank - 3

    elif action == "DOWN":
        new_blank = blank + 3

    elif action == "LEFT":
        new_blank = blank - 1

    else:
        new_blank = blank + 1

    state[blank], state[new_blank] = \
        state[new_blank], state[blank]

    return tuple(state)


def depth_limited_search(state, depth, previous_state):

    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)

    if state == goal_state:
        print("Goal Found!")
        print_state(state)
        return True

    if depth == 0:
        return False

    previous_state.append(state)

    for action in ACTIONS(state):

        new_state = RESULT(state, action)

        if new_state not in previous_state:

            print("Action:", action)
            print_state(new_state)

            if depth_limited_search(
                    new_state,
                    depth - 1,
                    previous_state):

                return True

    return False


def IDS(initial_state):

    depth = 0

    while True:

        print("Depth:", depth)

        previous_state = []

        if depth_limited_search(
                initial_state,
                depth,
                previous_state):

            return

        depth += 1


initial_state = (1, 2, 3,
                 4, 5, 6,
                 0, 7, 8)

print("Initial State:")
print_state(initial_state)

IDS(initial_state)