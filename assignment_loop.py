# Input a number
number = int(input("Enter a number: "))

# Display all the number up to number
for i in range(1, number+1):
    # stop if number>100
    if(i>100):
        break
    # skip the multiple of 10
    if(i%10!=0):
        print(i)