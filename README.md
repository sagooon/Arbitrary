# Arbitrary

A demonstration of an elementary project for initiating python programmers. Arbitrary is an elementary terminal game developed with the purpose to be used by initiating learners of python as a practice project. It is an uncomplicated script with less than 20 lines of code. Arbitrary import random module to create an unknown random number which is to be guessed by us. We get numbers from 1 to 99 to be chosen for guessing the unknown random number. We get infinite attempts for guessing the specific number. It's not so advanced but an appropriate project for python learners in the beginning stage. It was developed by [SaGoOn](http://sagooon.renderforestsites.com).

![Arbitrary](https://user-images.githubusercontent.com/74248485/98885322-eb4a5900-24b9-11eb-96f2-3dafedf511e5.png)


## Requirements

Latest version of [python](https://python.org) must be installed on your system including [pip](https://pypi.org/project/pip/) and [random](https://pypi.org/project/random-321/) module for running the program without any error. We recommend you to use [visual code studio](https://code.visualstudio.com/) as the text editor for programming. Also install python in visual code studio from extension panel. Make sure you setup these requirements for the best environment while programming.

## Basic Execution

```

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
             
print("Finally, you guessed it correct.")
