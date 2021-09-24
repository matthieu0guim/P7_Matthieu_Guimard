from typing import final
import pandas as pd

final_configuration = []
def knapstack(actions, profits, remaining_budget, item_number, chosen = None):
    global final_configuration
    if item_number == -1  or remaining_budget == 0:
        return 0, chosen
    elif actions[item_number][1] > remaining_budget:
        return knapstack(actions, profits, remaining_budget, item_number - 1), None
    else:
        left_choice, left_action = knapstack(actions,
                             profits,
                             remaining_budget,
                             item_number-1,
                             actions[item_number][0])
        right_choice, right_action =  knapstack(actions,
                                                profits,
                                                remaining_budget - actions[item_number][1],
                                                item_number-1,
                                                actions[item_number][0])
        right_choice += profits[item_number]
        if right_choice > left_choice:
            final_configuration.append(right_action)
            return right_choice, right_action
        else:
            decision = left_choice
            return left_choice, left_action
        # if max(skip_choice, take_choice[1]) == take_choice[1]:
        #     final_configuration.append(actions[item_number])
        #     return take_choice
        # else:
        #     return skip_choice

        # decision = max(knapstack(actions,
        #                      profits,
        #                      remaining_budget,
        #                      item_number-1),
        #                profits[item_number] + knapstack(actions,
        #                                                 profits,
        #                                                 remaining_budget - actions[item_number][1],
        #                                                 item_number-1))
        # if decision == profits[item_number] + knapstack(actions,
        #                                                 profits,
        #                                                 remaining_budget - actions[item_number][1],
        #                                                 item_number-1,
        #                                                 final_configuration):
            # print(actions[item_number])
        #     final_configuration.append(actions[item_number])
        return decision, chosen


first_tab = pd.read_csv("partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], first_tab.loc[i].values[2]) for i in range(len(first_tab))]
list_of_profits = [round(action[1] * action[2], 2) for action in list_of_actions]

liste =  [('Action_1', 20, 0.05), ('Action_2', 30, 0.1), ('Action_3', 50, 0.15), ('Action_4', 70, 0.2)]
revenus = [1.0, 3.0, 7.5, 14.0]

# print(list_of_actions)
# print(list_of_profits)

# a = knapstack(list_of_actions, list_of_profits, 500, len(list_of_actions)-1)
b = knapstack(liste, revenus, 100, len(liste)-1)
# print(a)
print(final_configuration)
print(b)
# print(final_configuration)
