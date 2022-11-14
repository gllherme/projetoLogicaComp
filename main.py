import csv

from semantics import *

patients = []
m = 1
signals = ['le', 'gt', 's']
atoms_list = []
array_filtered = []

with open("data/column_bin_3a_2p.csv", "r") as file:
    csv = csv.reader(file)
    i = 0
    for row in csv:
        if i == 0:
            attributes = row
        if i >= 1:
            patients.append(row)
        i += 1


def create_atoms():
    for index in range(m):
        for attr in attributes:
            if attr != 'P':
                for signal in signals:
                    created_atom = Atom('x_' + attr + '_' + str(index + 1) + '_' + signal)
                    atoms_list.append(created_atom)
    return atoms_list


def or_all(list_formulas):
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = Or(first_formula, formula)
    return first_formula


def and_all(list_formulas):
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = And(first_formula, formula)
    return first_formula


def filter_atoms():
    each_signal = int(len(atoms_list) / 3)
    size = len(atoms_list)
    for index in range(each_signal):
        start = int(index * size / each_signal)
        end = int((index + 1) * size / each_signal)
        array_filtered.append(atoms_list[start:end])
    return array_filtered


def restriction_1():
    list_complete = []
    for index in range(len(array_filtered)):
        list_atoms_splitted = array_filtered[index]
        list_1 = []
        list_2 = []
        for i in range(len(list_atoms_splitted)):
            for j in range(len(list_atoms_splitted)):
                if i != j:
                    list_1.append(
                        And(list_atoms_splitted[i], Not(list_atoms_splitted[j])))
            list_2.append(and_all(list_1))
            list_1 = []
        list_complete.append(or_all(list_2))
    return and_all(list_complete)


def restriction_2():
    or_list = []
    and_list = []
    for i in range(m):
        for atom in atoms_list:
            if "_s" in atom.name:
                or_list.append(Not(atom))
        or_list = or_all(or_list)
        and_list.append(or_list)
        or_list = []

    return and_all(and_list)


def restriction_3():
    or_list = []
    or_atoms = []
    for patient in patients:
        if patient[len(patient) - 1] == '0':
            for i in range(m):
                index = 0
                for attr in patient:
                    if attributes[index] != 'P':
                        if attr == '0':
                            or_atoms.append(Atom('x_' + attributes[index] + '_' + str(i + 1) + '_' + signals[0]))
                        if attr == '1':
                            or_atoms.append(Atom('x_' + attributes[index] + '_' + str(i + 1) + '_' + signals[1]))
                    index += 1
                or_atoms = or_all(or_atoms)
                or_list.append(or_atoms)
                or_atoms = []
    return and_all(or_list)


def restriction_4():
    patient_index = 0
    implies_list = []
    and_list = []
    for i in range(m):
        for patient in patients:
            if patient[len(patient) - 1] == '1':
                patient_index += 1
                c = Atom('c_' + str(i + 1) + '_' + str(patient_index))
                index = 0
                for attr in patient:
                    if attributes[index] != "P" and attr == "0":
                        implies_list.append(
                            Implies(Atom('x_' + attributes[index] + "_" + str(i + 1) + "_" + signals[0]), Not(c)))
                    if attributes[index] != "P" and attr == "1":
                        implies_list.append(
                            Implies(Atom('x_' + attributes[index] + "_" + str(i + 1) + "_" + signals[1]), Not(c)))
                    index += 1
                implies_list = and_all(implies_list)
                and_list.append(implies_list)
                implies_list = []
        patient_index = 0
    return and_all(and_list)


def restriction_5():
    patient_index = 1
    or_list = []
    or_atoms = []
    for patient in patients:
        if patient[len(patient) - 1] == '1':
            for i in range(m):
                or_atoms.append(
                    Atom('c_' + str(i + 1) + '_' + str(patient_index)))
            or_atoms = or_all(or_atoms)
            or_list.append(or_atoms)
            or_atoms = []
            patient_index += 1
    return and_all(or_list)


create_atoms()

array_filtered = filter_atoms()

final_formula = and_all([restriction_1(), restriction_2(), restriction_3(), restriction_4(), restriction_5()])

result = satisfiability_brute_force(final_formula)

if result:
    print(result)
else:
    print("conjunto de regras não se aplica ao paciente")
