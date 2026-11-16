
def unify(x, y, subst):

    if x == y:
        return subst

    if isinstance(x, str) and x.islower():
        return unify_var(x, y, subst)

    if isinstance(y, str) and y.islower():
        return unify_var(y, x, subst)

    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0] or len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):

            subst = unify(a, b, subst)

            if subst is None:
                return None

        return subst

    return None


def unify_var(var, x, subst):

    if var in subst:
        return unify(subst[var], x, subst)

    if isinstance(x, str) and x in subst:
        return unify(var, subst[x], subst)

    if occurs(var, x, subst):
        return None

    subst[var] = x

    return subst


def occurs(var, x, subst):

    if var == x:
        return True

    if isinstance(x, str) and x in subst:
        return occurs(var, subst[x], subst)

    if isinstance(x, tuple):
        return any(occurs(var, item, subst)
                   for item in x[1:])

    return False


# Main program
expr1 = ('Knows', 'x', 'Ram')
expr2 = ('Knows', 'Sita', 'y')

result = unify(expr1, expr2, {})

if result is None:
    print("Unification Failed")
else:
    print("Unification Successful")
    print("Substitution:", result)
