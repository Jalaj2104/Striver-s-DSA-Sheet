n = int(input("Enter a number"))
def printNum(i):
    if(i<1):
        return
    printNum(i-1)
    print(i)
printNum(n)