"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """
from functions import *


def truth_value(formula, interpretation):
    if isinstance(formula, Atom):
        return interpretation[str(formula)]

    if isinstance(formula, Not):
        return not truth_value(formula.inner, interpretation)

    if isinstance(formula, And):
        formula_left = truth_value(formula.left, interpretation)
        formula_right = truth_value(formula.right, interpretation)

        return formula_left and formula_right

    if isinstance(formula, Or):
        formula_left = truth_value(formula.left, interpretation)
        formula_right = truth_value(formula.right, interpretation)

        return formula_left or formula_right

    if isinstance(formula, Implies):
        formula_left = truth_value(formula.left, interpretation)
        formula_right = truth_value(formula.right, interpretation)

        if formula_left:
            return formula_right
        else:
            return True


def satisfiability_checking(formula, atoms_list, interpretation):
    # for atom in atoms_list:
    if not atoms_list:
        if truth_value(formula, interpretation):
            return interpretation
        else:
            return False

    atom = atoms_list.pop()
    interpretation1 = interpretation | {str(atom): False}
    interpretation2 = interpretation | {str(atom): True}

    result = satisfiability_checking(formula, atoms_list.copy(), interpretation1)
    if result:
        return result
    return satisfiability_checking(formula, atoms_list.copy(), interpretation2)


def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""

    interpretation = {}

    # obs.: a melhoria sugerida no vídeo, na verdade, aumenta o tempo de execução
    for subformula in subformulas(formula):
        if isinstance(subformula, And):
            interpretation = interpretation | satisfiability_brute_force(subformula.left)

    return satisfiability_checking(formula, atoms(formula), interpretation)
