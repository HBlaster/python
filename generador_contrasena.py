import random


def generar_contra():
    mayus= ['A','B','C','D','E','F','G','H','I','J']
    minus= ['a','b','c','d','e','f','g','h','i','j']
    simbol=['!','"','#','$','%','&','/','(',')','=','?','¿','¡', ' ']
    num = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayus + minus + simbol + num
    contrasena = []

    for i in range(15):
        caracter_rand = random.choice(caracteres)
        contrasena.append(caracter_rand)
    contrasena = ''.join(contrasena)
    return contrasena
    

def run():
    contrasena = generar_contra()
    print('Tu nueva contrasena es: "'+ contrasena +'"')
    print('***NO INCLUIR LAS COMILLAS DE LOS EXTREMOS***')


if __name__=='__main__':
    run()