# Write a program that takes integer input from the user and checks whether the number is even or odd using if-else statement and print the result.
# taking integer as input from user and storing it in variable num.
num=int(input('Enter the number to be checked: '))
# to check if given number is odd or even
#eqn: if number%2==0 then its even else odd
if (num % 2 == 0):
    print('Number: ', num, 'is even.')
else:
    print('Number: ', num, 'is odd.')