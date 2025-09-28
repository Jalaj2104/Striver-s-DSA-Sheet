n = int(input("Enter a number"))
i = 1
def printNum():
    global i
    if(i>n):
        return
    print(i)
    i += 1
    printNum()
printNum()
