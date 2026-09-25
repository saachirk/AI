# Vacuum Cleaner using Simple Reflex and Goal-Based Agent

rooms = {
    "A": "Dirty",
    "B": "Dirty"
}


# Simple Reflex Agent
def simple_reflex(location):
    if rooms[location] == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


# Goal-Based Agent
def goal_based(location):
    # Goal: Both rooms should be clean

    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        return "Goal Achieved"

    if rooms[location] == "Dirty":
        return "Suck"

    if location == "A":
        return "Move Right"
    else:
        return "Move Left"


# Main program
location = "A"

print("SIMPLE REFLEX AGENT")

for i in range(4):
    print("Location:", location)
    print("Rooms:", rooms)

    action = simple_reflex(location)
    print("Action:", action)

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"

    print()


# Reset rooms
rooms["A"] = "Dirty"
rooms["B"] = "Dirty"
location = "A"

print("GOAL-BASED AGENT")

while True:
    print("Location:", location)
    print("Rooms:", rooms)

    action = goal_based(location)
    print("Action:", action)

    if action == "Goal Achieved":
        print("Both rooms are clean!")
        break

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"

    print()