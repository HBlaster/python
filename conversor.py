from pydoc import doc

def operacion (moneda,mensaje):
    Pesos=float(input(mensaje))
    result= Pesos/moneda
    result= round(result,2)
    result= str(result)
    print('Usted tiene $ ' +result+ ' Dolares.')
    
i=True
while i==True:    
    menu= """
    Bienvenido al conversor de monedas 💰💎

    1- Pesos Mexicanos
    2- Pesos Colombianos
    3- Pesos Argentinos

    Elige una opcion: """

    moneda = int(input(menu))

    pesoMx_dolar=20.26
    pesoCo_dolar=4205.05
    pesoAr_dolar=125.42
    if moneda ==1:
        operacion (pesoMx_dolar,'Ingrese la cantidad en pesos mexicanos: ')    
        #Ciclo while
        print('Desea realizar otra operacion ? ')
        resp= int(input('(1: Si, 2: No)'))
        if resp ==1:
            i=True
        else:
            i=False
   

    elif moneda ==2:
        operacion (pesoCo_dolar,'Ingrese la cantidad en pesos Colombianos: ')  
        #Ciclo while
        print('Desea realizar otra operacion ? ')
        resp= int(input('(1: Si, 2: No)'))
        if resp ==1:
            i=True
        else:
            i=False

    elif moneda ==3:
        operacion (pesoAr_dolar,'Ingrese la cantidad en pesos Argentinos: ') 
        #Ciclo while  
        print('Desea realizar otra operacion ? ')
        resp= int(input('(1: Si, 2: No)'))
        if resp ==1:
            i=True
        else:
            i=False  

    else:
        print("Elige una opcion del menu")
        #Ciclo while
