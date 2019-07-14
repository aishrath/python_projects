def count(x):
  n = 1
  while n < int(x):
    print(n)
    n += 1
    if n == int(x):
      break
    else: 
      continue
x = input("What is your number?")

count(x)
