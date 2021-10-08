import pandas as pd
import numpy as np
import time

start = time.time()
config = []

"""big number of data"""
#todo demander le nom du fichier en ligne de commande
user_choice = input("Voulez-vous tester le dataset1 ou le dataset2?")

new_tab = pd.read_csv(f"data/{user_choice}_Python+P7.csv", sep=';', encoding='latin-1')
first_tab = new_tab.loc[new_tab['price'] > 0 | new_tab['name'].isnull() | new_tab['name'].isna()].reset_index()
list_of_actions = [(first_tab['name'][i], first_tab['price'][i], first_tab['profit'][i]) for i in range(len(first_tab))]
weights = [action[1]*100 for action in list_of_actions]
profits = [round(action[1] * action[2]/100, 2) for action in list_of_actions]
table = np.zeros((len(list_of_actions) + 1, 50001))

print(f" nombre de données avec un prix <= 0: {len(new_tab.loc[new_tab['price'] <= 0 | new_tab['name'].isnull() | new_tab['name'].isna()])}")
exit()
for i in range(0, len(list_of_actions) + 1):
    for j in range(0, len(table[0])):
        # base case
        if i == 0 or j == 0:
            continue # could have been table[i][j] = 0 but we already initiate the table at zeros for all cells
        elif weights[i-1] > j:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = max(table[i-1][j], profits[i-1] + table[i-1][int(j - weights[i-1])])

res = table[-1][-1]
W = len(table[0])
w = W - 1

# these lines are used to get the configuration back
for i in range(len(list_of_actions) , 0, -1):
    if i == 764:
        print(list_of_actions[i - 1][1] )

    if res <= 0 or list_of_actions[i - 1][1]*100 > w:
        break
    if res == table[i - 1][w]:
        continue
    else:
        print(f"i:{i}, w:{w}")
        print(f"action: {list_of_actions[i - 1]}, weight: {weights[i-1]}")
        res = res - profits[i - 1]
        w = int(w - weights[i - 1])
        config.append(list_of_actions[i - 1])


print(f"Le profit maximum réalisable est de: {round(table[-1][-1], 2)} \n pour un investissement de {sum([action[1] for action in config])}")
print(f"Avec l'achat des actions suivantes: {config}")
print(f"le programme de programmation dynamique met:{time.time() - start} secondes")