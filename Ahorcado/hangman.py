import random
import os


def generateWord():
    data=[]

    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append((line))

    randomWord= random.choice(data)
    return randomWord

def noCharacters(word):
    letters= (
        ("á","a"),
        ("é","e"),
        ("í","i"),
        ("ó","o"),
        ("ú","u"),   
    )

    for a,b in letters:
        word = word.replace(a,b)
    return word

def wordLength(word):
    length=len(word)-1  
    return length

GAME_OVER = """  
   ___             _ _     _         _  _  _ _
  / _ \___ _ __ __| (_)___| |_ ___  / \/ \/  / 
 / /_)/ _ \ '__/ _` | / __| __/ _ \/  /  /  /
/ ___/  __/ | | (_| | \__ \ ||  __/\_/\_/\_/ 
\/    \___|_|  \__,_|_|___/\__\___\/ \/ \/                                          
 """

WIN = """  
   ______                       __       ______
  / ____/___ _____  ____ ______/ /____  / / / /
 / / __/ __ `/ __ \/ __ `/ ___/ __/ _ \/ / / / 
/ /_/ / /_/ / / / / /_/ (__  ) /_/  __/_/_/_/  
\____/\__,_/_/ /_/\__,_/____/\__/\___(_|_|_)  
"""

def muneco(lifes):
    my_list_ASCII = ['''
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                  ========= ''', 
                  '''
                    +---+
                    |   |
                    O   |
                    |   |
                        |
                        |
                  ========= ''', 
                  '''
                    +---+
                    |   |
                    O   |
                   /|   |
                        |
                        |
                  ========= ''', 
                  '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                  ========= ''', 
                  '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   /    |
                        |
                  ========= ''', 
                  '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                  ========= ''']
    if lifes ==6:
        return my_list_ASCII[0]
    elif lifes ==5:
        return my_list_ASCII[1]
    elif lifes ==4:
        return my_list_ASCII[2]
    elif lifes ==3:
        return my_list_ASCII[3]
    elif lifes ==2:
        return my_list_ASCII[4]
    elif lifes ==1:
        return my_list_ASCII[5]

def figura(lifes):
    if lifes ==6:
        print(muneco(6))
    elif lifes ==5:
        print(muneco(5))    
    elif lifes ==4:
        print(muneco(4))
    elif lifes ==3:
        print(muneco(3))
    elif lifes ==2:
        print(muneco(2))
    elif lifes ==1:
        print(muneco(1))            





#Start
def run ():
    randomWord = str(generateWord())
    length = wordLength(randomWord)
    randomWord = noCharacters(randomWord)
    underScore=[]
    goAhead= True
    lifes=6
    var = 0
    backUpVar = var
    

    for i in range(length):
        underScore.append("_")
    underScore = list(underScore)

    while goAhead != False:
        os.system("cls")
        figura(lifes)
        

        print(f'Vidas restantes: {lifes}')
        print("Adivina la palabra: ")

        for i in range (length):
            print(underScore[i],)

        print(randomWord)#Eliminar este print cuando el juego este concluido
        print(length)

        selectedWord = input("Elige una letra: ")
        assert selectedWord.isalpha(), "Introduzca una letra, porfavor"

        while len(selectedWord)!=1:
            selectedWord=input("Elige solo una letra, porfavor: ")
            assert selectedWord.isalpha(), "Introduzca una letra, porfavor"
        for i in range (0,length):
            if randomWord[i]==selectedWord:
                underScore[i]=randomWord[i]
                print('acertaste')
                var+=1
                if var==length:
                    os.system("cls")
                    print(randomWord)
                    print(WIN)
                    goAhead=False
            
        if backUpVar ==var:
            lifes-=1
            if lifes ==0:
                goAhead=False
            if goAhead==False:
                os.system("cls")
                print(f'Vidas restantes: {lifes}')
                print(GAME_OVER)
                
                break
        else:
            backUpVar= var   
 

if __name__=='__main__':
    run()
