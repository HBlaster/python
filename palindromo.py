#Un palindromo es una aplabra que significa lo mismo al derecho y al reves
def palindromo (palabra):
    palabra = palabra.replace(' ','') #Eliminar los espacios de la palabra
    palabra = palabra.lower()
    palabra_invertida = palabra [::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False   


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo' )
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()