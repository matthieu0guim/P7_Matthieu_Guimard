import pandas as pd
import itertools
first_tab = pd.read_csv("partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], first_tab.loc[i].values[2]) for i in range(len(first_tab))]

# permutation = list(itertools.permutations(list_of_actions))
maximal_budget = 500
all_gain = set()
i = 0
for nb, configuration in enumerate(itertools.permutations(list_of_actions)):
    # if nb == 200000:
    #     break
    # else:
    #     # print(configuration)
    total = 0
    gain = 0
    all_actions = []
    i += 1
    
    for index, action in enumerate(configuration):
        if total + action[1] < maximal_budget:
            total += action[1]
            gain += action[1]*action[2]
        else:
            all_actions = configuration[:index]
            if gain not in all_gain:
                all_gain.add(round(gain, 2))
            break
    print(all_actions)
        
print(f"Cette configuration rapporte un gain de {round(gain,2)} euros")
print("fini")

        



# print(len(permutation))
# combinations_list = [i for i in itertools.chain(list_of_actions)]
# print(combinations_list)
# print(combinations_list[2])
