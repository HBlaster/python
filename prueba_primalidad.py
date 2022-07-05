from math import factorial


def es_primo(numero):
    # contador = 0

    # for i in range (1, numero+1):
    #     if i==1 or i==numero:
    #         continue
    #     if numero % i == 0:
    #         contador +=1
    # if contador == 0:
    #     return True
    # else:
    #     return False
    factorial = 1
    for i in range (1,numero):
        factorial = factorial*i
    if (factorial +1) % numero == 0:
        return True
    else:
        return False

def run():
    numero = int(input('Escrbie un numero: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('Es par')


if __name__=='__main__':
    run()