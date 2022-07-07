def run ():
    # dict ={}

    # for i in range (1,101):
    #     if i%3 !=0:
    #         dict[i]=i**3
    # print (dict)
    dictionary = {i : round(i**3,2) for i in range(1,101) if i%3 !=0}

    print(dictionary)

    challenge = {i : round(i**0.5,2) for i in range(1,1001) }

    print(challenge)



if __name__=='__main__':
    run()