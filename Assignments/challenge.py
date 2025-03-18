'''
#Celcius  ------------> Fahrenheit
c=input('Celcius: ')
c=float(c)
f=(c * 9/5) + 32
print('Fahrenheit: ',f )



#Fahrenheit  ---------------> Celcius
f=input('Fahrenheit: ')
f=float(f)
c=(f - 32) * 5/9
print('Celcius: ',c)

'''

#Simple Interest Calculator
#EQN: PNR/100
P=int(input('Enter the Principal amount: '))
R=int(input('Enter the Rate of Interest: '))
T=int(input('Enter the duration in years: '))

SI=(P * R * T)/100
print('Simple Interest is: ',SI)
