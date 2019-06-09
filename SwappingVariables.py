a = -4
b = -4
print(a)
print(b)
c = a
a = b
b = c
print(a)
print(b)

a = a + b
b = a - b
a = a - b

print(a)
print(b)

#If a or b exceed the size of computer words or if the sum (or difference if you reverse the operations) exceeds the limit for the computer you are using, this will not work. If these conditions are not exceeded, then it will work.
