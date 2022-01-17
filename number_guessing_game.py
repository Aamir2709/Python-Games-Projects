# -*- coding: utf-8 -*-
"""Number Guessing Game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cBKBPCfleApNn8pxiMiSxrL6lgmhnnY2

Number Guessing Game
"""

import sys
import random

l = int(input("Enter lower limit: "))
h = int(input("Enter higher limit: "))
x = random.randint(l,h)
i=8
c=0
while(i!=0):
    guess = int(input("{} chances left, Guess the number:  ".format(i)))
    if guess > x:
        print("A little lower please")
    elif guess < x:
        print("A little higher please ")
    elif guess ==x:
        print("Hurray!! you have guessed the number correctly in {} attempts".format(c+1))
        sys.exit()
    c+=1 
    i-=1
print("Oops!! your chances are over, the number was {}".format(x))