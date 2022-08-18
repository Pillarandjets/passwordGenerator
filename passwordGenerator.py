#Andrew Robinson
#Password Generator

import random
import time

#shuffle the characters in a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#generate each random character
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter3=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter4=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter5=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter6=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter7=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter8=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter9=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter10=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + uppercaseLetter7 + uppercaseLetter8 + uppercaseLetter9 + uppercaseLetter10 # + ....
password = shuffle(password)

#Ouput
print("Your randomly generated password: ")
time.sleep(0.5) 
print(password)