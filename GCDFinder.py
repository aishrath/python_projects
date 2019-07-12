def GCD(x,y):
 if number1 == 0 and number2 == 0:
   print("We cannot compute the GCD because both of your numbers are 0.")
 elif number1 == 0 and number2 > 0:
   print("The GCD of your numbers is " + str(number2) + ".")
 while x != y:
   if x > y:
     x = x - y
   else:
     y = y - x
 return(x)

number1 = int(input("What is your first whole number?"))
number2 = int(input("What is your second whole number?"))
a = GCD(number1,number2)
print(str(a))
print(str(GCD(number1,number2)))
