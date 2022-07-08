import random
import os



def generateWord():
    data=[]
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append((line))
    randomWord= random.choice(data)
    return randomWord

def wordLength(word):
     length=len(word)-1  
     return length


#Start
def run ():
    randomWord =str(generateWord())
    length = wordLength(randomWord)
    underScore=[]
    goAhead= True
    hits=4
    var = 0

    for i in range(length):
        underScore.append("_")
    underScore = list(underScore)

    while goAhead != False:
        print(f'Vidas restantes: {hits}')
        print("Adivina la palabra: ")
        for i in range (length):
            print(underScore[i],)
        print(randomWord)#Eliminar este print cuando el juego este concluido
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
                    goAhead=False
            
        if hits ==0:
            goAhead = False
        os.system("cls")
    print('Felicidades Ganaste!!')
    

    # print(selectedWord)



            

if __name__=='__main__':
    run()
