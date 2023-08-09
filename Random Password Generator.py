import random

#A function to do shuffling of all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Main program starts here
uppercaseLetter=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
lowercaseletter=chr(random.randint(97,122))
lowercaseletter2=chr(random.randint(97,122))
lowercaseletter3=chr(random.randint(97,122))
lowercaseletter4=chr(random.randint(97,122))
lowercaseletter5=chr(random.randint(97,122))
lowercaseletter6=chr(random.randint(97,122))
lowercaseletter7=chr(random.randint(97,122))
randomnumber=random.randint(0,9)
randomnumber2=random.randint(0,9)
randomnumber3=random.randint(0,9)
specialcharacter= "!@#$%^&*?.,`~'|=+-_"

#Generates the password using all the characters and numbers in a random order
password = uppercaseLetter + uppercaseLetter2 + lowercaseletter + lowercaseletter2 + lowercaseletter3 + lowercaseletter4 + lowercaseletter5 + lowercaseletter6 + lowercaseletter7 + str(randomnumber) + str(randomnumber2) + str(randomnumber3) + random.choice(specialcharacter)
password = shuffle(password)

#Output
print(password)