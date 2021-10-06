import pandas as pd
first_tab = pd.read_csv("partie_1.csv", sep=';', encoding='latin-1')
list_of_actions = [(first_tab.loc[i].values[0], first_tab.loc[i].values[1], first_tab.loc[i].values[2]) for i in range(len(first_tab))]


maximal_budget = 500
all_gain = set()
all_comb = []
H = 0

def f(k, liste, s):
    for n, i in enumerate(liste):
        global all_comb
        global all_gain
        # if k + i > 10:
        #     return f(k, liste[n+1:])
        # if k + i == 10:
        #     H += 1
        #     if len(liste[n:]) == 1:
        #         return 1
        #     else:
        #         return f(k, liste[n+1:])
        if s + i[1] <= 500:
            s += i[1]
            all_comb.append(i)
            # f(k, liste[n+1:], s)
        if s == 500:
            somme = 0
            for action in all_comb:
                somme += action[1]*action[2]
            all_gain.add(round(somme, 2))
            
            # return f(k, liste[n:])
def calcGain(liste):
    somme = 0
    for action in liste:
        somme += action[1]*action[2]
    return somme

def calcCost(liste):
    somme = 0
    for action in liste:
        somme += action[1]
    return somme

def final_function(liste):    
    global H
    for k in range(len(liste)):
        f(liste[k], liste[k:])
    print(H)

f(list_of_actions[0], list_of_actions, 0)
print(all_comb)
print(all_gain)

def f2(liste1, liste2):
     global all_comb
     if calcCost(liste2) > 500:
         liste2.pop()
         all