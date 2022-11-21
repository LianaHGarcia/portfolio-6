sentence = input("Please enter a sentence if your liking: ")
def obfuscation(sentence):
    sentence.replace(" ","") #removes spaces
    print(sentence[::-1]) #reverses the string

obfuscation(sentence)