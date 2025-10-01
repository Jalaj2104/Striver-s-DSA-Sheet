arr = list(map(int, input("Enter elements separated by space: ").split()))
k = int(input("Enter no. of operations"))
n = len(arr)
g = max(arr)
count = 0
s = 0
for i in range(n):
    if((g - arr[i]) <= k and s <= k):
        count += 1
        s = s + (g-arr[i])
print(count)
