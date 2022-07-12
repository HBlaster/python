import time
import sys
sys.setrecursionlimit(1000000) #Modificar el numero de veces que se puede hacer uso de la recursividad

def factorial(n):
    respuesta = 1

    while n>1:
        respuesta = respuesta * n
        n-=1
    return respuesta


def factorialR(n):
    if n == 1:
        return 1
    
    return n * factorialR(n-1)


if __name__=='__main__':
    n = 1000

    #Probar cual algoritmo es mas rapido
    comienzo = time.time() # iniciar el temporizador
    print(factorial(n))
    final = time.time() # Detener el cronometro
    print(final - comienzo)
    print('')
    comienzo = time.time() # iniciar el temporizador
    print(factorialR(n))
    final = time.time() # Detener el cronometro
    print(final - comienzo)


    #Clases de complejidad algoritmica:
    #   O(1)     Constante
    #   O(n)     Lineal
    #   O(log n) log lineal
    #   O(n**2)  Polinomial
    #   O(2**n)  Exponencial
