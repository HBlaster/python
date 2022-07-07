from functools import reduce


def run():
    #Imprimir numeros impares con list  comprehensions
    list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,58,258,96]
    odd = [i for i in list_1 if i%2!=0]
    print(odd)
    print(' ')

    #Filter hacer un cambio en un punto especifico
    odd = list(filter(lambda x: x%2 !=0, list_1))

    print(odd)
    print(' ')

    #map hacer un cambio en todos los elementos
    squares = list(map(lambda x: x**2, list_1))
    print(squares)
    print(' ')

    #Reduce
    list_2 = [1,2,3,4,5,6]
    all_multiplied = reduce (lambda a,b: a*b, list_2)

    print(all_multiplied)

if __name__=='__main__':
    run()
