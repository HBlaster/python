#para hacer una busqueda binaria se necesita que la lista este ordenada
import imp


import random
def busqueda_binaria (lista, comienzo, final, objetivo):
    print(f'Buscando {objetivo} en una lista entre {lista[comienzo]} hasta {lista[final-1]}')
    medio = ( comienzo + final) // 2 #Se usa la division con doble divisor para que solo regrese numeros enteros
    if comienzo > final:
        return False
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio +1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo)        

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista =sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    
    print (lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no se encuentra"} en la lista')