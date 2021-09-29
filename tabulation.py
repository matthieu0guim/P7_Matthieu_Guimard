import pandas as pd
import numpy as np
import time

start = time.time()

"""test case"""
# actions = [('Action_1', 20, 0.05), ('Action_2', 30, 0.1), ('Action_3', 50, 0.15), ('Action_4', 70, 0.2)]
# weights = [i[1] for i in actions]
# profits = [i[1] * i[2] for i in actions]
# table = np.zeros((len(actions) + 1, 10))
# print(table)

"""realistic case"""
first_tab = pd.read_csv("partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], first_tab.loc[i].values[2]) for i in range(len(first_tab))]
weights = [action[1] for action in list_of_actions]
profits = [round(action[1] * action[2], 2) for action in list_of_actions]
table = np.zeros((len(list_of_actions) + 1, 500))

# for i in range(0, len(actions) + 1):
for i in range(0, len(list_of_actions) + 1):
    for j in range(0, len(table[0])):
        # base case
        if i == 0 or j == 0:
            continue # could have been table[i][j] = 0 but we already initiate the table at zeros for all cells
        elif weights[i-1] > j:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = max(table[i-1][j], profits[i-1] + table[i-1][j - weights[i-1]])

print(f"maximum profit: {table[-1][-1]}")
print(f"le programme de programmation dynamique met:{time.time() - start} secondes")