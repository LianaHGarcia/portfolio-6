string = input("Please enter a sentence if your liking: ")
def char_insert(string):
    hidden_message = 'ab'.join(string[i:i+2] for i in range (0,len(string),2))
    print("the new message is: ", hidden_message)
char_insert(string)