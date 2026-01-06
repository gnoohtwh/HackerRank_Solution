import math
# n =  46934
# m = 543563655

# s = 46743
n = 7
m = 25
s = 6
step = m % n-1 # ignoring the first candy at prisoner(n)
if step + s > n:
    print(s+step -n)
else:
    print(s+step)
