fib = []
fib.append(0)
print(fib)
fib.append(1)
print(fib)

for i in range (2,1000):
  fib.append(fib[i-2]+fib[i-1])
  i = i + 1

print(fib)
