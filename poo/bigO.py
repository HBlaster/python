# Ley de la multiplicacion
def f(n):
    for i in range(n):
        for j in range(n):
            print(f'valor de i: {i}, valor de j: {j}')

    print('')
    print(f'valor final de i: {i}, valor final de j: {j}')
#O(n) * O(n) = O(n*n) = 0(n**2)


#Recursividad multiple:
def fibonacci(n):
    if n==0 or n==1:
        return 1
    return fibonacci(n-1) + fibonacci (n-2)
#O(2**n)


if __name__=='__main__':
    n = f(10)

