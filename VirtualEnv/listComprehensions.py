def run():
    # my_list = []
    # for i in range(1,101):
    #     my_list.append(i**2)
    # print(my_list)

    # my_list=[]
    # for i in range (1,101):
    #     if i % 3 != 0:
    #         my_list.append(i**2)  
    # print(my_list)
    # print(' ')

    #List Comprehensions

    # my_list=[i**2 for i in range (1,101) if i % 3 !=0]

    # print(my_list)

    #Reto

    challenge = [ i for i in range (1,100000) if i%4==0 and i%6==0 and i%9==0 ]
    print(challenge)




    


if __name__=='__main__':
    run()
