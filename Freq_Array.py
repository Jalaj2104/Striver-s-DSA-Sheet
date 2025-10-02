nums = list(map(int, input("Enter elements separated by space: ").split()))
freq = {}                     
for num in nums:              
    if num in freq:           
        freq[num] += 1        
    else:                     
        freq[num] = 1         
result = []                   
for key in freq:              
    result.append([key, freq[key]])  
print(result)                 
