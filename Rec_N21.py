n = int(input("Enter a number"))
i = n
def revNum():
    global i
    if(i == 0):
        return
    print(i)
    i -= 1
    revNum()
revNum()