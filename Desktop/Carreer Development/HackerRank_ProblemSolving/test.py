# for loop to count how many 'a' character in len(s)->  -> while loop used to divide n by k until n < len(s) (using altNum for n new container) 
# Checking if string s is empty
s = "ababa"
if len(s) == 0:
    print(0)


# Counting how many 'a' character in the string s
n = 3
aCount  = 0 # how many 'a'character are there in string s?
count = 0 

if n >= len(s):
    for c in s:
        if c == 'a':
            aCount += 1
    while n >= len(s):
        count += (n // len(s)) * aCount
        rem = n % len(s)

        if rem == 0:
            break
        else:
            if rem < len(s):
                for i in range(rem):
                    if s[i]== 'a':
                        count += 1
                break
            elif rem >= len(s):
                n = rem 
else:
    for i in range(n):
        if s[i] == 'a':
            count +=1
print(count)

