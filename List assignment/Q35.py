#35. Create a list and remove all even numbers

numbers = [10, 15, 20, 25, 30, 35, 40]

new_list = []

for num in numbers:
    if num % 2 != 0:
        new_list.append(num)

print("List without Even Numbers:", new_list)