def divisors(num):
    divisors = []
    for i in range (1, num+1):
        if num %i ==0:
            divisors.append(i)
    return divisors

#Try, except error handling
def run():
        num = input('Ingresa un numero entero: ')
        assert num.isnumeric(), "Debes ingresar numeros positivos"
        print(divisors(int(num)))
        print('Programa termino')

if __name__=='__main__':
    run()