liste = [6, 5, 3, 2]
H = 0

def f(k, liste):
    global H
    for n, i in enumerate(liste):
        # print(f"{k} + {i} = {k + i}") 
        if k + i > 10:
            return f(k, liste[n+1:])
        if k + i == 10:
            H += 1
            if len(liste[n:]) == 1:
                return 1
            else:
                return f(k, liste[n+1:])
        if k + i < 10:
            f(k + i, liste[n:])
        else:
            return f(k, liste[n:])
def final_function(liste):    
    global H
    for k in range(len(liste)):
        f(liste[k], liste[k:])
    print(H)
final_function(liste)
