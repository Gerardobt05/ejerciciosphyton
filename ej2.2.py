edad = 0
print("DIme la edad del niño:")
edad = int(input())

if(edad < 6):
    print("El niño no tiene categoría deportiva")
elif(edad == 6 or edad==7):
    print("La categoría del niño es BENJAMÍN")
elif(edad == 8 or edad ==9):
    print("La categoría del niño es ALEVÍN")
elif(edad == 10 or edad ==11):
    print("La categoría del niño es INFANTIL")
else:
    print("La categoría es CADETE")