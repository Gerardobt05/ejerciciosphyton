"""
Definir una función que devuelva una lista con 20 números random
"""
#lista_numeros()
#devuelve por ejemplo ---> [2,4,7,8,9,11,14,15,18,19,20]
import random
def lista_numeros():
    lst = []
    for i in range(0,20):
        numAle = random.randint(0,100)
        lst.append(numAle)
        
    return lst_pares

"""
Definir una función que devuelva una lista que filtre los números pares
"""

def filtra_lista_pares(lst):
    lst_pares = []
    for i in lst:
        if(i % 2 == 0):
            lst_pares.append(i)
        
    return lst
            