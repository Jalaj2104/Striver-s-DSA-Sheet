arr = list(map(int, input("Enter numbers: ").split()))
n = len(arr)
print("Your array :", arr)
def RevArr(i):
    if (i >= (n/2)):
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return RevArr(i+1)
RevArr(0)
print("Reversed Array: ", arr)



