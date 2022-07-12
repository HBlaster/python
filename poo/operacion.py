from re import X


def f(x):
    respuesta = 0
    for i in range(x):
        print (f'respuesta i(uno): {respuesta}')
        for j in range(x):
            respuesta +=1
            respuesta +=1
            print (f'respuesta j(dos): {respuesta}')

if __name__=='__main__':
    x = f(10)
    print(x) 
