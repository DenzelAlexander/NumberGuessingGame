#!/bin/python3

from random import randint


print("Welcome to Random Number Guesser")
y = int(randint(1,100))
print (y)
x = 0
while (x != y):
    print ("Please enter a value (1-100)")
    x = int(input())
    if (x>y):
        print ("Too high")
    if (x<y):
        print ("Too low")
    if ((abs(x-y)<10) & x-y != 0): 
        print ("Very close!")
print("You won!")