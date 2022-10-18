# Introduciendo la hora del día en horas, minutos y segundos, calcular cuantos segundos han transcurrido desde el comienzo del día
# Definir las entradas
hora = 0
minutos = 0
segundos = 0

# Pedir al usuario que ingrese la hora, los minutos y los segundos
hora = int(input("DIme la hora: "))
minutos = int(input("DIme los minutos: "))
segundos = int(input("DIme los segundos: "))

# Realizamos la operación
hora = hora * 3600
minutos = minutos * 60
segundos = segundos + minutos + hora

# Mostramos el resultados
print("Han transcurrido desde el inicio del día", segundos, " segundos.")