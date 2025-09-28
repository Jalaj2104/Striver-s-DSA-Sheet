n = str(input("Enter your name"))
N = int(input("Enter a number"))
count = 0
def printName():
    global count
    if(count == N):
        return
    print(n)
    count += 1
    printName()
printName()