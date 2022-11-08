from formulas import *


def length(formula):
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1


def subformulas(formula):
    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)


def atoms(formula):
    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula.inner}
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        atom_array = []
        for subformula in subformulas(formula):
            if isinstance(subformula, Atom):
                atom_array.append(subformula)
        return atom_array

