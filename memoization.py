import pandas as pd
import numpy as np
import time

start = time.time()
final_configuration = []
first_tab = pd.read_csv("partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], first_tab.loc[i].values[2]) for i in range(len(first_tab))]
list_of_profits = [round(action[1] * action[2], 2) for action in list_of_actions]
table = np.ones((500, len(list_of_actions)))

def memoization(actions, profits, remaining_budget, item_number, element_selection = []):
    global final_configuration
    global table
    if item_number == -1  or remaining_budget == 0:
        return 0
    if table[remaining_budget][item_number] != 1:
        return table[remaining_budget][item_number]
    if actions[item_number][1] > remaining_budget:
        return memoization(actions, profits, remaining_budget, item_number - 1, element_selection)[0]

    else:
        left_choice = memoization(actions,
                                profits,
                                remaining_budget,
                                item_number-1,
                                element_selection
                                )[0]
        right_choice =  profits[item_number] + memoization(actions,
                                                           profits,
                                                           remaining_budget - actions[item_number][1],
                                                           item_number-1,
                                                           element_selection + [actions[item_number]]
                                                          )[0]
        table[remaining_budget][item_number] = max(left_choice, right_choice)
        return (table[remaining_budget][item_number], element_selection)

a = memoization(list_of_actions, list_of_profits, 499, len(list_of_actions)-1)
print(a)
end = time.time()
print(f"Avec memoization le programme met {end - start} à s'éxécuter")

