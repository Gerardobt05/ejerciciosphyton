# EJ 3.3 : Imprimir en pantalla el número mayor y el número menor de una serie de cinco números enteros que vamos introduciendo por teclado.


import math

min_ = math.inf
max_ = (-1) * math.inf
contador = 5
num = -1

while(contador > 0):
    num = int(input("Dime un número:"))
    
    if(num < min_ ):
        min_ = num
        
    if(num > max_):
        max_ = num
        
    contador -= 1
    
print("El máximo es: ", max_)
print("El mínimo es: ", min_) 
