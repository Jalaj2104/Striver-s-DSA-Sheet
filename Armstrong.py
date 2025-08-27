n = int(input("Enter a number"))
original = n
ans = 0
if(n>0):
    while(n!=0):
        d = n % 10
        ans = d**3 + ans
        q = n // 10
        n = q
    if(original == ans):
        print(True)
    else:
        print(False)