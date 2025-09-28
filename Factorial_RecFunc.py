n = int(input("Enter a number"))
def Factorial(i):
    if(i == 0):
        return 1
    return i * Factorial(i-1)
print(Factorial(n))