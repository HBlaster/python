from encodings import utf_8

#r=read a=append

def read():#Leer un archivo .txt 
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f: #Abrir un archivo
        for line in f:
            numbers.append(int(line))
    print (numbers)

def write():#Escribir un archivo .txt
    names= ["José","Alfredo","Paulina","Lili","Mili","Maya","José","Alfredo","Paulina"]
    with open("./files/names.txt", "a", encoding="utf_8") as f:
        for name in names:
            f.write(name)
            f.write("\n")



def run():
    write()
    # read()
    


if __name__=='__main__':
    run()