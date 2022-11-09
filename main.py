from functions import *
from formulas import *
from semantics import *


formula1 = Atom('p')  # p
formula2 = Atom('q')  # q
formula3 = And(formula1, formula2)  # (p /\ q)
formula4 = And(Atom('p'), Atom('s'))  # (p /\ s)
formula5 = Not(And(Atom('p'), Atom('s')))  # (¬(p /\ s))
formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))  # ((¬(p /\ s)) v q)
formula7 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Atom('r')))  # ((¬(p /\ s)) -> (q /\ r))
formula8 = Implies(Not(And(Atom('p'), Atom('s'))),
                   And(Atom('q'), Not(And(Atom('p'), Atom('s')))))  # ((¬(p /\ s)) -> (q /\ (¬(p /\ s))))


interpretation = {'p': True, 'q': False, 's': True, 'r': False}

print(truth_value(formula7, interpretation))