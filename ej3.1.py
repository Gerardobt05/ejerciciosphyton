# Introduciendo un número en el teclado, imprimir la tabla de multiplicar de dicho número.

resultado = -1
indice = 0
numero = -1

print("Dime un número:")
numero = int(input())
print("La tabla del ", numero)

while(indice <= 10):
    resultado = numero * indice
    print(numero, " x ", indice , " = ", resultado)
    indice = indice + 1
    
print("FIN")