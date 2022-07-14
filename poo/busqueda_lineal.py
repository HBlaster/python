import random
import time

def busqueda_lineal(lista, objetivo):
    match = False
    cont = 0
    for elemento in lista: # O(n)
        cont +=1
        print(f'Esta es la {cont} iteracion')
        if elemento == objetivo:
            match = True
            break
        
    return match


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    comienzo = time.time()
    encontrado = busqueda_lineal(lista, objetivo)
    print (lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no se encuentra"} en la lista')
    final = time.time()
    print(f'El tiempo de ejecucion del algoritmo fue {round((final - comienzo),10)}')