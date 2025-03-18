#Write a program to take first and last name as input from user and print a personalized greeting message using full name.

#Taking first and last name as input from user and storing in variables first and last respectively.
first=input('Enter your first name: ')
last=input('Enter your last name: ')
#Concatenating first and last and storing value in variable full.
full = first + " " + last
#printing personalized greeting message using full name
print("Hello, " + full + "! Welcome to the Python program.")
