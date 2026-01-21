import math as m
k= 7
s= [278,576,496,727,410,124,338,149,209,702,282,718,771,575,436]


s = [num%k for num in s] # Creating a list with all the remaining num after divide it to k 
s = sorted(s)
print(s)
res = 0

if s[0] == 0: # If any of those numbers can be divided by k, it will just make the res + 1, but why ? -> because the maximize num cointaing in a subset is only 1 (if there are more than 1 number in that subset, it makes the subset invalid)
    res += 1

sDict = {}
for num in s:
    if num != 0:
        if num in sDict:
            sDict[num] += 1
        else:
            sDict[num] = 1 
# Creating the list to count how many num by each categories 
s = list(sDict.items())
print(s)
#binary search the max length of total sub that can not be divided by k
l, r = 0, len(s)-1
while l <= r:
    if s[l][0]+s[r][0] == k:
        if s[l][0] == k/2:
            res += 1
        else:
            if s[l][1] > s[r][1]: # Maximizing the length of the subset
                res += s[l][1]
            else:
                res += s[r][1]
        r -= 1
        l += 1     
    else:
        if s[l][0]+s[r][0] > k: # Maximizing the length of the subset
            res += s[r][1]
            r -= 1
        else:
            res += s[l][1]
            l += 1
    

# print(res)