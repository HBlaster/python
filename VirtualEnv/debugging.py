def divisors(num):
    divisors = []
    for i in range (1, num+1):
        if num %i ==0:
            divisors.append(i)
    return divisors

#Try, except error handling
def run():
    try:
        num = int(input('Ingresa un numero entero: '))
        print(divisors(num))
        print('Programa termino')
    except ValueError:
        print("Debes ingresar un numero")


if __name__=='__main__':
    run()