from random import randint


def run ():
    numero = int(input('Elige un numero del 1 al 100: '))
    random = randint(1,100)
    #print(str(random))
    while numero != random:
        if random > numero:
            print('Elige un numero mas grande')
        elif random < numero:
            print('Elige un numero mas pequeño')
        numero = int(input('Elige otro numero: '))
    print('Ganaste!!')


if __name__=='__main__':
    run()