#capacity
C = int(input ())

#students
A = int(input())

#number of travels
V = A/(C-1)
V2= A//(C-1)

if (V > V2):
    V2 = V2 + 1

print (V2)


