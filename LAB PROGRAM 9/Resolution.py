
def unify(a, b, subst={}):
    subst = subst.copy()

    for x, y in zip(a, b):
        if x.startswith("?"):
            subst[x] = y
        elif y.startswith("?"):
            subst[y] = x
        elif x != y:
            return None

    return subst


def apply(clause, subst):
    result = []

    for neg, pred, args in clause:
        args = tuple(subst.get(x, x) for x in args)
        result.append((neg, pred, args))

    return result


def resolve(c1, c2):
    for l1 in c1:
        for l2 in c2:

            n1, p1, a1 = l1
            n2, p2, a2 = l2

            if p1 == p2 and n1 != n2:

                subst = unify(a1, a2)

                if subst is not None:
                    new_clause = [
                        x for x in c1 if x != l1
                    ] + [
                        x for x in c2 if x != l2
                    ]

                    return apply(new_clause, subst), subst

    return None, None


def display(clause):
    if not clause:
        return "{}"

    parts = []

    for neg, pred, args in clause:
        s = pred + "(" + ",".join(args) + ")"

        if neg:
            s = "~" + s

        parts.append(s)

    return " V ".join(parts)


# CNF Clauses

A = [
    (True, "Food", ("?x",)),
    (False, "Likes", ("John", "?x"))
]

B = [(False, "Food", ("Apple",))]

C = [(False, "Food", ("Vegetables",))]

D = [
    (True, "Eats", ("?y", "?z")),
    (False, "Killed", ("?y",)),
    (False, "Food", ("?z",))
]

E = [(False, "Eats", ("Anil", "Peanuts"))]

F = [(False, "Alive", ("Anil",))]

G = [
    (True, "Eats", ("Anil", "?w")),
    (False, "Eats", ("Harry", "?w"))
]

H = [
    (False, "Killed", ("?g",)),
    (False, "Alive", ("?g",))
]

I = [
    (True, "Alive", ("?k",)),
    (True, "Killed", ("?k",))
]

# Negated Goal
J = [(True, "Likes", ("John", "Peanuts"))]


clauses = [A, B, C, D, E, F, G, H, I, J]

print("GIVEN CNF CLAUSES:\n")

for name, clause in zip("ABCDEFGHIJ", clauses):
    print(name + ".", display(clause))


print("\n\nRESOLUTION PROOF:\n")

# Step 1: J + A
c1, s1 = resolve(J, A)

print("1. J + A")
print("   Substitution:", s1)
print("   Result:", display(c1))


# Step 2: D + C1
c2, s2 = resolve(D, c1)

print("\n2. D + Result 1")
print("   Substitution:", s2)
print("   Result:", display(c2))


# Step 3: C2 + E
c3, s3 = resolve(c2, E)

print("\n3. Result 2 + E")
print("   Substitution:", s3)
print("   Result:", display(c3))


# Step 4: C3 + I
c4, s4 = resolve(c3, I)

print("\n4. Result 3 + I")
print("   Substitution:", s4)
print("   Result:", display(c4))


# Step 5: C4 + F
c5, s5 = resolve(c4, F)

print("\n5. Result 4 + F")
print("   Substitution:", s5)
print("   Result:", display(c5))


if c5 == []:
    print("\n{} Hence Proved!")
else:
    print("\nGoal not proved")
