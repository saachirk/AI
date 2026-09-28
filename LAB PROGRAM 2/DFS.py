def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def ACTIONS(initial_state):
    actions = []
    blank = initial_state.index(0)
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

    elif action == "RIGHT":
        new_blank = blank + 1

    state[blank], state[new_blank] = \
        state[new_blank], state[blank]

    return tuple(state)



def goal_based_DFS(initial_state,previous_state):
    goal_state = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
    if initial_state == goal_state:
        print("Goal Found")
        print_state(initial_state)
        return True

    
    previous_state.append(initial_state)
    
    for action in ACTIONS(initial_state):
        new_state = RESULT(initial_state,action)

        if new_state not in previous_state:

            print("Action:", action)
            print_state(new_state)
            
            if goal_based_DFS(new_state,previous_state):
                return True

    return False

initial_state = (1, 2, 3,
                 4, 5, 6,
                 0, 7, 8)

previous_data = list()

if goal_based_DFS(initial_state, previous_data):
    print("Goal Found")
else:
    print("Goal Not Found")
