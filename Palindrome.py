s = str(input("Enter a string"))
arr = list(s)
n = len(arr)
def checkPal(i):
    if (i >= n-i-1):
        return
    if( arr[i] == arr[n-i-1]):
        i += 1
        checkPal(i)
        return True
    else:
        return False
result = checkPal(0)
print(result)
