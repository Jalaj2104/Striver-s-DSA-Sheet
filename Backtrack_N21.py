n = int(input("Enter a number"))
def revNum(i):
    if(i>5):
        return
    revNum(i+1)
    print(i)
revNum(1)
