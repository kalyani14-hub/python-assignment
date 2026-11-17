#33.Create a list and find the second largest number

numbers = [10, 50, 30, 80, 40]

new_list = sorted(set(numbers))

second_largest = new_list[-2]

print("Second Largest Number:", second_largest)