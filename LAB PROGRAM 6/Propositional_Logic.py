
from itertools import product

def KB(model):
    P = model['P']
    Q = model['Q']

    return (not P or Q) and P


def Query(model):
    return model['Q']


def TruthTableEntails(KB, Query, symbols):

    for values in product([True, False], repeat=len(symbols)):

        model = dict(zip(symbols, values))

        if KB(model) and not Query(model):
            return False

    return True


symbols = ['P', 'Q']

print("P\tQ\tKB\tQuery")

for values in product([True, False], repeat=2):
    model = dict(zip(symbols, values))

    print(model['P'], model['Q'], KB(model),
          Query(model), sep='\t')


if TruthTableEntails(KB, Query, symbols):
    print("\nKB entails Query")
else:
    print("\nKB does not entail Query")
