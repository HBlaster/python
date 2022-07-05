def run ():
    print('Cuales son sus nombres ? ')

    nom_1 = input('Nombre 1: ')
    nom_2 = input('Nombre2: ')
    edad_1= int(input(f'Que edad tienes, {nom_1} ?' ))
    edad_2= int(input(f'Que edad tienes, {nom_2} ?'))

    if edad_1<edad_2:
        print(nom_1 + ' Es menor que ' + nom_2)

    elif edad_1>edad_2:
        print(nom_1 + ' Es mayor que ' + nom_2)
    else:
        print('Son de la misma edad.')
            

if __name__=='__main__':
    run()