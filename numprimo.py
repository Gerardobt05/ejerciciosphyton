#Decir si un número es primo o no primo
'''index = 1000
while(index>0):
    index = index - 1
    print(index)'''

'''
index = 2
num = -1
esPrimo = True

num = int(input("Dime un número: "))

while(num > index):
    if(num % index == 0):
        esPrimo = False
        break
    else:
        index += 1
        
print(esPrimo)'''


def esPrimo(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    
    return True




'''
Realizar un programa que nos diga los primos que se encuentran entre 1 y 1000
'''
'''
def primeros1000primos():
    lst = []
    for i in range(1,1001):
        if(esPrimo(i)):
            lst.append(i)
    
    return lst
        
            
print(primeros1000primos())
'''
def primeros1000primos_while():
    i = 1
    lst = []
    while(i<1000):
        if(esPrimo(i)):
            lst.append(i)
        i = + 1
        
                
        
            
        
        

        
        