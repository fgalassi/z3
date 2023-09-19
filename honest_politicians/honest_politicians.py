from z3 import *

# From https://www.philipzucker.com/using-z3-solve-simple-logic-puzzle/

# There are 100 politicians
politicians = [ Bool('x%s' % i) for i in range(100)]

# True -> Honest
# False -> Crooked

# At least one is honest
at_least_one_politician_is_honest = Or(politicians)

# For any two at least one is crooked
for_any_two_politicians_at_least_one_is_crooked = And(
    [Or(Not(i), Not(j)) for i in politicians for j in politicians if not i is j]
)

s = Solver()
s.add(at_least_one_politician_is_honest)
s.add(for_any_two_politicians_at_least_one_is_crooked)
s.check()
model = s.model()
honest_men = len(tuple(filter(lambda x: model[x], model.decls())))
crooked_men = 100 - honest_men

print('Honest men: %d' % honest_men)
print('crooked men: %d' % crooked_men)
