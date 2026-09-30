"""
Question 1: Personal Greeting
Write a Python program that asks the user for their name using the `input` function. Store the name in a variable, and then print a greeting message that includes the name. For example, if the user enters "Ankit", the program should print "Hello, Ankit!".


"""

name = (input("Enter your name :"))

print("Hello,",name)


"""
Question 2: Age in Years
Create a Python program that prompts the user to enter their age in years using the `input` function. Convert this age from a string to an integer and store it in a variable. Then, calculate and print the age in months (assume 12 months in a year). For example, if the user enters "20", the program should output "You are 240 months old."

"""

age = int(input("Enter Your Age :"))

age_in_months = age * 12

print("Your age in months is : ",age_in_months)