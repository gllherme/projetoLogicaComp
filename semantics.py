"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from formulas import *
from functions import atoms


def truth_value(formula, interpretation):
    if isinstance(formula, Atom):
        return interpretation[str(formula)]


    if isinstance(formula, Not):
        return not truth_value(formula.inner, interpretation)
        
        
    if isinstance(formula, And):
        formulaLeft = truth_value(formula.left, interpretation)
        formulaRight = truth_value(formula.right, interpretation)
        
        return formulaLeft and formulaRight
    
    
    if isinstance(formula, Or):
        formulaLeft = truth_value(formula.left, interpretation)
        formulaRight = truth_value(formula.right, interpretation)
        
        return formulaLeft or formulaRight
    
    
    if isinstance(formula, Implies):
        formulaLeft = truth_value(formula.left, interpretation)
        formulaRight = truth_value(formula.right, interpretation)
        
        if formulaLeft:
            return formulaRight
        else: 
            return True
        
    
def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========

