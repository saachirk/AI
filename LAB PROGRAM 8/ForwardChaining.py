
def match(pattern, fact, subst):
    if pattern[0] != fact[0]:
        return None

    subst = subst.copy()

    for p, f in zip(pattern[1:], fact[1:]):
        if p.startswith("?"):
            if p in subst and subst[p] != f:
                return None
            subst[p] = f
        elif p != f:
            return None

    return subst


def solve(premises, facts, subst=None):
    if subst is None:
        subst = {}

    if not premises:
        return [subst]

    results = []

    first = premises[0]

    for fact in facts:
        new_subst = match(
            tuple(subst.get(x, x) for x in first),
            fact,
            subst
        )

        if new_subst is not None:
            results.extend(
                solve(premises[1:], facts, new_subst)
            )

    return results


def forward_chaining(facts, rules, goal):

    facts = set(facts)

    print("Initial Facts:", facts)

    while True:
        new_facts = set()

        for premises, conclusion in rules:

            substitutions = solve(premises, facts)

            for subst in substitutions:

                result = tuple(
                    subst.get(x, x) for x in conclusion
                )

                if result not in facts:
                    new_facts.add(result)
                    print("Inferred:", result)

                if result == goal:
                    return True

        if not new_facts:
            break

        facts.update(new_facts)

    return goal in facts


# Initial facts
facts = [
    ("American", "Robert"),
    ("Owns", "A", "T1"),
    ("Missile", "T1"),
    ("Enemy", "A", "America")
]


# Rules
rules = [

    (
        [
            ("American", "?p"),
            ("Weapon", "?q"),
            ("Sells", "?p", "?q", "?r"),
            ("Hostile", "?r")
        ],
        ("Criminal", "?p")
    ),

    (
        [
            ("Missile", "?x"),
            ("Owns", "A", "?x")
        ],
        ("Sells", "Robert", "?x", "A")
    ),

    (
        [("Missile", "?x")],
        ("Weapon", "?x")
    ),

    (
        [("Enemy", "?x", "America")],
        ("Hostile", "?x")
    )
]


# Goal
goal = ("Criminal", "Robert")

print("\nForward Chaining:")

if forward_chaining(facts, rules, goal):
    print("\nGoal Proved:", goal)
else:
    print("\nGoal Cannot Be Proved")
