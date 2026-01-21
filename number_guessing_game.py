import random 

secret_number = random.randint(1,10)
number= int(input ("Enter your  number (1-10) : "))
if number ==secret_number:
    print ("Correct, you guessed a number", secret_number)
else:
    print ("Wrong, The correct number was  ", secret_number)
