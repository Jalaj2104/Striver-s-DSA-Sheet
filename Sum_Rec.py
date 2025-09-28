n = int(input("Enter a number"))
def Sum(i,s):
    if(i > n):
        return s
    return Sum(i+1,s+i)
result = Sum(1,0)
print("The sum from 1 to", n ,"is", result)


