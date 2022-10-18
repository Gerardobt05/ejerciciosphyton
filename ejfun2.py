# Introducir un número y devolver la suma de sus dígitos
'''Ejemplo suma_digitos(234) = 9'''

'''def suma_digitos(numero):
    resultado = 0
    str_numero = str(numero)
    
    for i in str_numero:
        resultado += int(i)
        
     return resultado
    
print(suma_digitos(234))   '''

#Devolver la suma de los diez primeros números naturales
'''
num = 0
index = 0

while(index <= 10):
    num += index
    index += 1
    
print("EL total es:", num)
'''
#Devolver la suma de los n primeros números naturales
def suma_total(n):
    contador = 0
    acumulador = 0
    while(contador < n):
        contador += 1
        acumulador += contador
      return acumulador  
    
    
num = int(input("Dime un número: "))
print()