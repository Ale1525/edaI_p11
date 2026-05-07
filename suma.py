#Diseña un algoritmo recursivo wue calcula la sumade los primeros nùmeros n naturales

#A)Escribe el caso base
#B)Escribe el caso recursivo
#C)Escuebtra la ecuacion de recurrencia
#D)Encuentra la complejidad del algoritmo

def Sum_natural(n):
    if n == 1:
        return 1

    return n + Sum_natural(n-1)

n = int(input("Ingresa el numero natural: "))

resultado = Sum_natural(n)
print("El resultado es", resultado)

#C) T(n)=1



diseña un algoritmo recursirvo que imprima todos los elementos de un alrreglo