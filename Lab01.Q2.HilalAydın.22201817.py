# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:58:37 2023

@author: hilala-ug
"""

"""
Write a program Lab01_Q2.py to input a playing card in the following shorthand notation:
A Ace D Diamond
2...10 Card values H Hearts
J Jack S Spades
Q Queen C Clubs
K King
The program should print the full description of the card. Assume that the user input is valid.
Sample Run:
Enter the card notation: JS
Jack of Spades
Sample Run:
Enter the card notation: 10H
10 of Hearts
Sample Run:
Enter the card notation: 2D
2 of Diamonds
Sample Run:
Enter the card notation: AC
Ace of Clubs
"""

card= input("Enter the card notation: ")

#Seperating the card shapes and its numbers by using string index
first_var = card[-3:-1]
second_var = card[-1]

#firstly defining second variale to use it within the next if statement
if second_var == "S":
    second_var= "Spades"
elif second_var == "C":
    second_var= "Clubs"
elif second_var== "H":
    second_var= "Hearts"
elif second_var== "D":
    second_var="Diamonds"
    
    
if first_var=="A":
   print("Ace of "+ second_var)
elif first_var== "J":
   print("Jack of " + second_var)
elif first_var== "Q":
   print("Queen of " + second_var)
elif first_var=="K":
    print("King of " + second_var)
else:
    print(first_var + " of " + second_var)




