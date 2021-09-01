import itertools
class Action():
    def __init__(self, nom, cout, rendement):
        self.nom = nom
        self.cout = cout
        self.revenu = self.cout * rendement

def taken(action, budget, revenu, configuration):
    budget += action.cout
    revenu += action.revenu
    configuration.append((budget, revenu))
    return budget, revenu

def not_taken(action):
    return
def make_instance(a):
    a = Action(a[0], a[1], a[2])
    return a

actions = [('Action_1', 20, 0.05), ('Action_2', 30, 0.1), ('Action_3', 50, 0.15), ('Action_4', 70, 0.2)]
a = list(map(make_instance, actions))
configurations, config2 = [], []
budget = 0
revenu = 0

def parcours(liste, configurations):
    for n, action in enumerate(liste):
        configurations.append([(action.nom, action.cout, action.revenu)])
    return configurations

def parcours2(liste, configurations):
    # configurations.append([(i1.nom, i1.cout, i1.revenu), (i2.nom, i2.cout, i2.revenu)] for i1 in liste[:-2] for i2 in liste[-2:])
    for k,i1 in enumerate(liste[0:3]):
        for i2 in liste[k+1:]:
            # if i1 == i2:
            #     continue
            configurations.append([(i1.nom, i1.cout, i1.revenu),(i2.nom, i2.cout, i2.revenu)])

def parcours3(liste, configurations):
    for k1, i1 in enumerate(liste[0:2]):
        for i2 in liste[k1+1:3]:
            k2 = liste.index(i2)
            for i3 in liste[k2+1:]:
                configurations.append([(i1.nom, i1.cout, i1.revenu),
                                       (i2.nom, i2.cout, i2.revenu),
                                       (i3.nom, i3.cout, i3.revenu)])



# parcours(a, configurations)
# parcours2(a, configurations)
# parcours3(a, configurations)
# print(configurations)



def recursion(config2, liste, n): # le paramètre n indique qu'on veut les combinaisons de 1 parmis len(liste) à n parmis len(liste)
    if n > len(liste):
        return 
    elif n == 0:
        return liste
    else:
        for n, action in enumerate(liste):
            listeG = liste[liste.index(action) + 1:]
            # print(f"listeG: {listeG}")
            config2.append([action.nom, action.cout, action.revenu])
            # print(f"liste2 : {config2}")
            recursion(config2, listeG, n-1)

recursion(config2, a, 3)
print(config2)


# def recursion2(liste, n):
#     for i in range(len(liste)):
#         if n == 1:
#             # yield ((liste[i].nom, liste[i].cout, liste[i].revenu),)
#             yield (liste[i][0],)
#         else:
#             for next in recursion2(liste[i+1:len(liste)], n - 1):
#                 yield (liste[i],) + next
# config3 = []
# liste_exemple = ["A", "B", "C", "D"]
# for k in range(1, len(a)):
#     config3.append(list(recursion2(actions, k)))
# print(config3)

def recursion3(config3, liste, n):
    if n == 1:
        print(config3)
    else:
        for i in range(len(liste)):
            new_liste = liste[i+1:]
            config3.append(liste[i])
            recursion3(config3, new_liste, n-1)

config3 = []
liste_exemple = ["A", "B", "C", "D"]
recursion3(config3, liste_exemple, 1)

# def comb(sofar, rest, n):
#     if n == 0:
#         print(sofar)
#     else:
#         for i in range(len(rest)):
#             comb(sofar + rest[i], rest[i+1:], n-1)

# comb("", "abcde", 3)