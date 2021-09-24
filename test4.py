import pandas as pd
first_tab = pd.read_csv("partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], first_tab.loc[i].values[2]) for i in range(len(first_tab))]


def marre(liste, n, p):
    i, imax = 0, 2**len(liste) - 1
    while i <= imax:
        s = []
        j, jmax = 0, len(liste) - 1
        while j <= jmax:
            if (i>>j)&1 == 1:
                s.append(liste[j])
            j += 1
        if len(s) == n:
            p.append(s)
        i += 1
    return p

liste =  [('Action_1', 20, 0.05), ('Action_2', 30, 0.1), ('Action_3', 50, 0.15), ('Action_4', 70, 0.2)]
revenus = [1.0, 3.0, 7.5, 14.0]
print(revenus)
# budget = 60
comb = []
# for i in range(1, 5):
#     marre(liste, i, comb)
    # marre(list_of_actions, i, comb)

# for i in comb:
#     print(i)
