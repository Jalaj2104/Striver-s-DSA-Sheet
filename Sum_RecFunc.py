n = int(input("Enter a number"))
def Sum(i):
    if(i == 0):
        return 0
    return i + Sum(i-1)
print(Sum(n))
