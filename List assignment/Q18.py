#18. Take user input of data and display it

my_list = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = input("Enter element: ")
    my_list.append(value)

print("Entered List:", my_list)