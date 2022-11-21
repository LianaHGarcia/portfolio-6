num = int(input("Please enter a number: "))
def prime_num(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
            else:
                print(num, "is a prime number")
                break

    else:
        print("Please enter a number greater than 1")

prime_num(num)