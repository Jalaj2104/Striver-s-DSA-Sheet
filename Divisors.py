import math
n = int(input("Enter a number"))
r = int(math.sqrt(n))
arr = []
for i in range(2,r+1):
    if(n%i == 0):
        if(n/i == i):
            arr.append(i)
        else:
            arr.extend([i,n/i])
arr.extend([1,n])
arr.sort()
print(arr)