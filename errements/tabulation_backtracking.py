import pandas as pd
import numpy as np
import time

start = time.time()
config = []
"""test case"""
# actions = [('Action_1', 20, 0.05), ('Action_2', 30, 0.1), ('Action_3', 50, 0.15), ('Action_4', 70, 0.2)]
# weights = [i[1] for i in actions]
# profits = [i[1] * i[2] for i in actions]
# table = np.zeros((len(actions) + 1, 100))
# heigh = len(table)
# length = len(table[0]) 
# print(table)

"""realistic case"""
first_tab = pd.read_csv("data/partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], first_tab.loc[i].values[2]) for i in range(len(first_tab))]
weights = [action[1] for action in list_of_actions]
profits = [round(action[1] * action[2], 2) for action in list_of_actions]
table = np.zeros((len(list_of_actions) + 1, 501))
print(f"{len(table)}, {len(table[0])}")
"""big number of data"""
# new_tab = pd.read_csv("dataset2_Python+P7.csv", sep=',', encoding='latin-1')
# # # print(f"new_tab: \n {new_tab}")
# first_tab = new_tab.loc[new_tab['price'] > 0].reset_index() #= 600 # some values are <= 0 so i replace this value with a price higher that our budget
# # # print(f"first_tab: \n {first_tab}") #.loc[first_tab['price'] <= 0].shape)
# list_of_actions = [(first_tab['name'][i], first_tab['price'][i], first_tab['profit'][i]) for i in range(len(first_tab))]
# # print(list_of_actions)
# weights = [action[1]*100 for action in list_of_actions]
# profits = [round(action[1] * action[2]/100, 2) for action in list_of_actions]
# table = np.zeros((len(list_of_actions) + 1, 50001))


# for i in range(0, len(actions) + 1):
for i in range(0, len(list_of_actions) + 1):
    for j in range(0, len(table[0])):
        # base case
        if i == 0 or j == 0:
            continue # could have been table[i][j] = 0 but we already initiate the table at zeros for all cells
        elif weights[i-1] > j:
            table[i][j] = table[i-1][j]
        else:
            # print(int(j - weights[i-1]))
            table[i][j] = max(table[i-1][j], profits[i-1] + table[i-1][int(j - weights[i-1])])

res = table[-1][-1]
W = len(table[0])
w = W - 1
# for i in range(len(actions) , 0, -1):
for i in range(len(list_of_actions) , 0, -1):
    
    if res <= 0 or list_of_actions[i - 1][1] > w:
        break
    if res == table[i - 1][w]:
        pass
    else:
        print(f"i:{i}, w:{w}")
        print(f"action: {list_of_actions[i - 1]}, weight:{weights[i - 1]}")
        config.append(list_of_actions[i - 1])
        res = res - profits[i - 1]
        w = int(w - weights[i - 1])
        # config.append(actions[i - 1])
            


print(f"maximum profit: {table[-1][-1]}")
print(config)
print(f"investissement de: {sum([action[1] for action in config])}")
print(f"le programme de programmation dynamique met:{time.time() - start} secondes")