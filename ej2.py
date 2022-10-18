# Escriba, usando comparaciones, un algoritmo que muestre el estado del agua (hielo, liquido, vapor) en función de su temperatura

temp = 0


temp = float(input("Dime la temperatura:"))

if (temp < 0):
    print(temp, " Es sólido ")

else:
    if (temp <= 100):
        print(temp, " Es liquido ")
    else:
        print(temp, " es gaseoso")
        
    
