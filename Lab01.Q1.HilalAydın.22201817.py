
"""
Write a program Lab01_Q1.py to input the meal purchased at a restaurant. The program
should calculate the total amount of the meal with a 15% percent tip and 8% sales tax. The
program should print the following:
● Meal
● Tip Amount
● Sales Tax
● Total
Sample Run:
Enter meal amount(in dollars): 50
Meal: $ 50.0
Tip Amount: $ 7.5
Sales Tax: $ 4.0
Total: $ 61.5
"""
meal_purchased= float(input("Enter meal amount(in dollars): "))
#taking input as float because the sample run has float outcomes

#calculating the desired percentages
tip = meal_purchased*0.15 
sales_tax = meal_purchased*0.08

total = meal_purchased + tip + sales_tax

print(f"Meal: $ {meal_purchased} ")
print(f"Tip Amount: $ {tip}")
print(f"Sales Tax: $ {sales_tax}")
print(f"Total: $ {total}")