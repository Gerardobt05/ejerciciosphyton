# Programa que dado dos parametros de entrada diga cual es mayor y cual es menor de ellos.

def mayor_menor(a, b):
    if(a>b):
       print("a:", a, "es mayor que b: ", b)
      
    else:
        print("b:", b, "es mayor que a: ", a)
           
pass

# Programa que dado tres números como parametros de entrada diga cual es el mayor.
def mayor_menor_3(a ,b ,c):
    if(a>b and a>c):
        print("a:", a, "es mayor que b: ", b, "y c: ", c)
    elif(c>a and c>b):
        print("c:", c, "es mayor que a: ", a, "y b: ", b)
    else:
        print("b:", b, "es mayor que a: ", a, "y c: ", c)
        pass



# Programa que intercambia los valores de entrada

def intercambia(a,b):
    print("a: ", a, "b:" , b)
    aux = b
    b = a
    a = aux
    print("a: ", a, "b:" , b)   


intercambia(4,2)