from semantics import *
from datetime import datetime

formula1 = Atom('p')  # p
formula2 = Atom('q')  # q
formula3 = And(formula1, formula2)  # (p /\ q)
formula4 = And(Atom('p'), Atom('s'))  # (p /\ s)
formula5 = Not(And(Atom('p'), Atom('s')))  # (¬(p /\ s))
formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))  # ((¬(p /\ s)) v q)
formula7 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Atom('r')))  # ((¬(p /\ s)) -> (q /\ r))
formula8 = Implies(Not(And(Atom('p'), Atom('s'))),
                   And(Atom('q'), Not(And(Atom('p'), Atom('s')))))  # ((¬(p /\ s)) -> (q /\ (¬(p /\ s))))
formula9 = And(Not(Atom('p')), Atom('q'))  # ((¬p) ∧ q)
formula10 = And(Atom('p'), And(Not(Atom('q')), Or(Atom('r'), Atom('s'))))  # (p ∧ ((¬q) ∧ (r ∨ s)))

formulas = [formula1, formula2, formula3, formula4, formula5, formula6, formula7, formula8, formula9, formula10]

start = datetime.now()
for formula in formulas:
    print(satisfiability_brute_force(formula))
stop = datetime.now()
print(stop - start)
