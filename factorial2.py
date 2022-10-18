# Recursividad

def factorial_rec(n):
    if(n == 0):
        return 1
    elif(n == 1):
        return 1
    else:
        return n * factorial_rec(n-1)
N = 6
print("El factorial de ", N, " es " , factorial_rec(N))