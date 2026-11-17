#37. Create a list and check palindrome list

my_list = [1, 2, 3, 2, 1]

if my_list == my_list[::-1]:
    print("List is Palindrome")
else:
    print("List is Not Palindrome")