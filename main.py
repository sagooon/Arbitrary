import random

secret_number=random.randrange(1,100)
user_input=None
guessses=0
while(secret_number!=user_input):
    guessses+=1
    user_input=int(input("Guess a number betweeen 1 to 99 --> "))
    if secret_number==user_input:
         print("Yes, you guessed it correct.") 
    elif secret_number>user_input:
          print("No, You guessed it incorrect. Try greater numbers.")
    else:
          print("No, You guessed it incorrect. Try smaller numbers.")
     
guessses=str(guessses)         
print("Finally, you guessed it correct.")

