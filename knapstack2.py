import pandas as pd
import numpy as np
import time
from exo2_arbres_livres import BinaryTree

start = time.time()
final_configuration = []
def knapstack(actions, profits, remaining_budget, item_number, current_tree):
    global final_configuration
    if item_number == -1  or remaining_budget == 0:
        return 0
    if actions[item_number][1] > remaining_budget:
        result = knapstack(actions, profits, remaining_budget, item_number - 1, current_tree)
        return result
    else:
        left_choice = [actions[item_number], knapstack(actions,
                                profits,
                                remaining_budget,
                                item_number-1,
                                current_tree)] 
        current_tree.insertLeft(left_choice[0])
        right_choice =  [actions[item_number], profits[item_number] + knapstack(actions,
                                                         profits,
                                                         remaining_budget - actions[item_number][1],
                                                         item_number-1,
                                                         current_tree)]
        current_tree.insertRight(right_choice[0])
        result = max(left_choice[1], right_choice[1])
        if result == left_choice[1]:
            current_tree = current_tree.getLeftChild()
            return result
        elif result == right_choice[1]:
            # print(right_choice[0])
            current_tree = current_tree.getRightChild()
            # current_tree.config.append(f"right choice: {right_choice[0]}")
    return result
        
def get_configuration(current_tree, remaining_budget, item_number, configuration):
    if current_tree.config[item_number][1] > remaining_budget:
        return configuration
    configuration.append(current_tree.config[item_number])
    return get_configuration(current_tree,
                             remaining_budget - current_tree.config[item_number][1],
                             item_number - 1,
                             configuration)
    

first_tab = pd.read_csv("partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], first_tab.loc[i].values[2]) for i in range(len(first_tab))]
list_of_profits = [round(action[1] * action[2], 2) for action in list_of_actions]
our_tree = BinaryTree('config')
a = knapstack(list_of_actions, list_of_profits, 500, len(list_of_actions)-1, our_tree)
print(a)
end = time.time()
print(f"Avec récursion, le programme met {end - start} à s'éxécuter")
# final_configuration = get_configuration(our_tree, 50, len(our_tree.config) - 1, [])
# print(final_configuration)
# print(our_tree.config)


# print(our_tree.getLeftChild().getRootVal())

# liste =  [('Action_1', 20, 0.05), ('Action_2', 30, 0.1), ('Action_3', 50, 0.15), ('Action_4', 70, 0.2)]
# revenus = [1.0, 3.0, 7.5, 14.0]
# our_tree = BinaryTree('config')
# b = knapstack(liste, revenus, 100, len(liste)-1, our_tree)
# print(b)
# # final_configuration = get_configuration(our_tree, 100, len(our_tree.config) - 1, [])
# print(final_configuration)


def get_tree(tree, liste):
    res1 = None
    res2 = None
    if tree:
        res1 = get_tree(tree.getLeftChild())
        res2 = get_tree(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()


        