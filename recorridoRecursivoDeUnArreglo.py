#diseña un algoritmo recursirvo que imprima todos los elementos de un alrreglo

#A)Escribe el caso base
#B)Escribe el caso recursivo
#C)Escuebtra la ecuacion de recurrencia
#D)Encuentra la complejidad del algoritmo

def imp_arr(arr, i):
    if i == len(arr):
        return
    

    print(arr[i])

    imp_arr(arr, i +1)

arr = [10, 20, 30, 40, 50]
imp_arr(arr, 0)

#A) i== 0
#B) i+1
#C) T(n) = T(n - 1)+1
#D)T(n) + T(n - 1) = 1
# si T(n) = x^1

diseña ul algoritmo recursirvo que imprima una cadena al revez
