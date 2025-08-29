n = int(input("Enter a number"))
arr = []
i = 1
for i in range(1,n+1):
    if(n%i == 0):
        arr.append(i)
print(arr)
