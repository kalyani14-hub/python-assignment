#19. Create a list of 10 numbers and remove duplicates

numbers = [10, 20, 30, 10, 40, 20, 50, 30, 60, 10]

new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print("List without duplicates:", new_list)