import random

numAleatorio = random.randint(0,100)
vidas = 3
print(numAleatorio)
while(vidas > 0):
    numUsuario = int(input("Dime un número: "))
    if(numUsuario != numAleatorio):
        vidas = -1
        
        if(vida != 1):
            print("Te quedan ", vidas, " oportunidades:")
        else:
            
            