num = int(input("Please enter a number: "))
print("The factors of", num, "are:")
def factors(num):
    if num > 1:
        for i in range(1,num+1):
            #the factors will only go as high as the number inputted
            if num % i == 0:
                #if there are no remainders when divided then thats the factor
                print(i)

    else:
        print("Please enter a number greater than 1")


factors(num)