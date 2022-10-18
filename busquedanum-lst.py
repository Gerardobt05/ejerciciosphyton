"""
Definir una función que devuelva una lista y un número que devuelva
"""

def busqueda_num(lst,num):
    for i in lst:
        if(i == num):
            return True
    return False


print(busqueda_num([1,2,3],3))
print(busqueda_num([1,2,3],8))
print(busqueda_num([12,5,8],5))
