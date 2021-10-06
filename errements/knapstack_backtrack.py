import pandas as pd
import numpy as np
import time

start = time.time()
final_configuration = []
def knapstack(actions, profits, remaining_budget, item_number, back_track=False, element_selection = []):
      
    if item_number == -1  or remaining_budget == 0:
        return 0
    if actions[item_number][1] > remaining_budget:
        result = knapstack(actions, profits, remaining_budget, item_number - 1, element_selection)
        return result
    else:
        left_choice = knapstack(actions,
                                profits,
                                remaining_budget,
                                item_number-1,
                                element_selection
                                )
        right_choice =  profits[item_number] + knapstack(actions,
                                                        profits,
                                                        remaining_budget - actions[item_number][1],
                                                        item_number-1,
                                                        element_selection + [actions[item_number]]
                                                        )
        result = max(left_choice, right_choice)
    return result
            
def from_str_to_number(string):
    """take a string as a+b+c+...
    split each value into a list and make the sum"""
    return sum([float(i) for i in string.split("+")])


first_tab = pd.read_csv("partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], first_tab.loc[i].values[2]) for i in range(len(first_tab))]
list_of_profits = [round(action[1] * action[2], 2) for action in list_of_actions]
a = knapstack(list_of_actions, list_of_profits, 500, len(list_of_actions)-1)
print(a)
end = time.time()
print(f"Avec récursion, le programme met {end - start} à s'éxécuter")



        