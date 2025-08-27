x,y = map(int,input("Enter 2 numbers").split())
rem = 1
if(y>x):
    while (rem>0): 
        rem = y%x
        y = x
        x = rem
    print(f"HCF is {y}")
else:
    while(rem>0):
        rem = x%y
        x = y
        y = rem
    print(f"HCF is {x}")        
    
    

