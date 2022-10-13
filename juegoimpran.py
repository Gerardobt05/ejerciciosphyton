import random

numeroaleatorio = random.randint(0,100)
num = -1
num = int(input("Dime un número: "))

if(num == numeroaleatorio):
    print("¡Has acertado!")
    
else:
    num2 = -1
    num2 = int(input("Has fallado, tienes dos oportunidades, dime otro número: "))
    
    if(num2 == numeroaleatorio):
        print("¡Has acertado!")
    else:
        num3 = -1
        num3 = int(input("Has vuelto a fallar, tienes una oportunidad, dime otro número: "))
        
        if(num3 == numeroaleatorio):
            print("¡Has acertado!")
        else:
            print("¡Has fallado!")

        
print(numeroaleatorio)