arr = list(map(int, input("Enter elements separated by space: ").split()))
n = len(arr)
g = max(arr)
#Precomputing
hash = [0]*(g+1)   
for i in range(n):
    hash[arr[i]] += 1 
print(hash)
