#40. Create a list and demonstrate all list methods

numbers = [30, 10, 20, 40]

# 1. append()
numbers.append(50)
print("Append:", numbers)

# 2. extend()
numbers.extend([60, 70])
print("Extend:", numbers)

# 3. insert()
numbers.insert(1, 15)
print("Insert:", numbers)

# 4. remove()
numbers.remove(15)
print("Remove:", numbers)

# 5. pop()
numbers.pop()
print("Pop:", numbers)

# 6. index()
print("Index of 30:", numbers.index(30))

# 7. count()
numbers.append(30)
print("Count of 30:", numbers.count(30))

# 8. sort()
numbers.sort()
print("Sort:", numbers)

# 9. reverse()
numbers.reverse()
print("Reverse:", numbers)

# 10. copy()
new_list = numbers.copy()
print("Copy:", new_list)

# 11. clear()
numbers.clear()
print("Clear:", numbers)