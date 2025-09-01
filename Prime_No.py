import math
n = int(input("Enter a number"))
if(n == 1):
    print("Unique No.")
r = int(math.sqrt(n))
prime = True
for i in range(2,r+1):
    if(n%i == 0):
        prime = False
        break
if prime:
    print("Prime")
else:
    print("Composite")