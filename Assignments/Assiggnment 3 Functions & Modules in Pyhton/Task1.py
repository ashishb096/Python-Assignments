def factori(n):
    fact=1
    n=int(n)
    for i in range(n):
        fact=fact*(i+1)

    return fact


n= input("Enter the number to generate factorial:")
factorials=factori(n)
print("Factorial is:\t", factorials)
