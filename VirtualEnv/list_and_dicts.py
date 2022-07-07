def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstName": "Alfredo", "LastName":"Cano"}

    #Lista de diccionarios
    super_list = [
        {"firstName": "Alfredo", "LastName":"Cano"},
        {"firstName": "Jose", "LastName":"Castro"},
        {"firstName": "Maria", "LastName":"Lopez"},
        {"firstName": "Lupe", "LastName":"Carso"},
        {"firstName": "Pedro", "LastName":"Carozo"}
    ]
    
    #Diccionario de listas
    super_dict = {
        "naturalNums":[1, 2, 3, 4, 5],
        "integerNums":[-1, -2, 0, 1, 2],
        "floatingNums":[1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')

    for i in super_list:
        print("Nombre:", i["firstName"], i["LastName"])


if __name__=='__main__': 
    run()
