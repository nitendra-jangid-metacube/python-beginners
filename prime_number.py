num = int(input("Enter a number: "))

primeFlag = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        primeFlag = False

if primeFlag==True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")