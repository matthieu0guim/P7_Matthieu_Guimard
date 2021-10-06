import pandas as pd
import numpy as np
import time

first_tab = pd.read_csv("data/partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], round(first_tab.loc[i].values[2] * first_tab.loc[i].values[1], 2)) for i in range(len(first_tab))]
list_of_profits = [round(action[1] * action[2], 2) for action in list_of_actions]

"""test case"""
# actions = [('Action_1', 20, 1), ('Action_2', 30, 3), ('Action_3', 50, 7.5), ('Action_4', 70, 14)]

start = time.time()


def sac_dos(capacite, elements, element_selection = []):
    if elements:
        val1, lstVal1 = sac_dos(capacite, elements[1:], element_selection)
        val = elements[0]
        if val[1] <= capacite:
            val2, lstVal2 = sac_dos(capacite - val[1], elements[1:], element_selection + [val])
            if val1 < val2:
                return val2, lstVal2
        return val1, lstVal1
    else:
        return round(sum([i[2] for i in element_selection]), 2), element_selection

a = sac_dos(500, list_of_actions)
print(a)

print(f"Avec combinaison restaurée, le programme prend {time.time() - start}s")

print(f"investissment de {sum([action[1] for action in a[1]])}")

