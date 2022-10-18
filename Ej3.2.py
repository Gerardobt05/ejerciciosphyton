# Ej 3.2.
# Inicializo las variables

total_multiplos = 0
numero = -1
index = 1

# Pregunto al usuario el número
numero = int(input("Dime un número: "))

while(index <= numero):
    if(index % 3 == 0):
        total_multiplos += 1
        
    index += 1
    
print("Entre la unidad y el número ", numero, " hay un total de ", total_multiplos,"multiplos de 3")