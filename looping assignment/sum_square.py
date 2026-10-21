#Calculate sum of square of first n numbers
n = int(input("Enter number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i *i
print("Sum of square= ",sum)