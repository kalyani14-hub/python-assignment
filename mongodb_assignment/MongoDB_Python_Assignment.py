from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
client.admin.command("ping")

db = client["college"]
students = db["students"]

print("\nMongoDB connected successfully!")

# SECTION A: DATABASE AND COLLECTION OPERATIONS

# Task 1: Create or select database
print("\nTASK 1: Select Database")
print("Database name:", db.name)


# Task 2: Create collection
print("\nTASK 2: Create Collection")

if "students" not in db.list_collection_names():
    db.create_collection("students")
    print("Collection created successfully")
else:
    print("Collection already exists")


# Task 3: Display all collections
print("\nTASK 3: Display Collections")
print(db.list_collection_names())


# Task 4: Insert one student
print("\nTASK 4: Insert One Student")

result = students.insert_one({
    "name": "Rahul",
    "age": 21,
    "marks": 78,
    "department": "Computer",
    "city": "Pune",
    "gender": "Male",
    "fees": 45000,
    "isActive": True
})

print("Inserted ID:", result.inserted_id)


# Task 5: Insert multiple students
print("\nTASK 5: Insert Multiple Students")

student_list = [
    {
        "name": "Amit",
        "age": 22,
        "marks": 65,
        "department": "IT",
        "city": "Mumbai",
        "gender": "Male",
        "fees": 40000,
        "isActive": True
    },
    {
        "name": "Rohit",
        "age": 20,
        "marks": 32,
        "department": "Computer",
        "city": "Pune",
        "gender": "Male",
        "fees": 35000,
        "isActive": False
    },
    {
        "name": "Sneha",
        "age": 21,
        "marks": 88,
        "department": "Computer",
        "city": "Pune",
        "gender": "Female",
        "fees": 42000,
        "isActive": True
    },
    {
        "name": "Priya",
        "age": 23,
        "marks": 92,
        "department": "IT",
        "city": "Nashik",
        "gender": "Female",
        "fees": 48000,
        "isActive": True
    },
    {
        "name": "Karan",
        "age": 20,
        "marks": 55,
        "department": "Mechanical",
        "city": "Mumbai",
        "gender": "Male",
        "fees": 52000,
        "isActive": False
    },
    {
        "name": "Anjali",
        "age": 22,
        "marks": 75,
        "department": "Computer",
        "city": "Pune",
        "gender": "Female",
        "fees": 39000,
        "isActive": True
    }
]

result = students.insert_many(student_list)
print("Inserted documents:", len(result.inserted_ids))


# SECTION B: READ AND DISPLAY OPERATIONS

# Task 6: Display all students
print("\nTASK 6: Display All Students")

for student in students.find():
    print(student)


# Task 7: Display only first 5 students
print("\nTASK 7: First 5 Students")

for student in students.find().limit(5):
    print(student)


# Task 8: Find students whose age is greater than 20
print("\nTASK 8: Age Greater Than 20")

for student in students.find({"age": {"$gt": 20}}):
    print(student)


# Task 9: Find students whose marks are greater than 75
print("\nTASK 9: Marks Greater Than 75")

for student in students.find({"marks": {"$gt": 75}}):
    print(student)


# Task 10: Find students from Computer department
print("\nTASK 10: Computer Department")

for student in students.find({"department": "Computer"}):
    print(student)


# Task 11: Find students from Pune city
print("\nTASK 11: Students From Pune")

for student in students.find({"city": "Pune"}):
    print(student)


# Task 12: Display only name and marks
print("\nTASK 12: Display Name and Marks")

for student in students.find(
    {},
    {"_id": 0, "name": 1, "marks": 1}
):
    print(student)


# Task 13: Find female students
print("\nTASK 13: Female Students")

for student in students.find({"gender": "Female"}):
    print(student)


# Task 14: Find students whose fees are less than 50000
print("\nTASK 14: Fees Less Than 50000")

for student in students.find({"fees": {"$lt": 50000}}):
    print(student)


# Task 15: Find active students
print("\nTASK 15: Active Students")

for student in students.find({"isActive": True}):
    print(student)


# =====================================================
# SECTION C: FILTERING AND SORTING
# =====================================================

# Task 16: Find students whose marks are between 60 and 90
print("\nTASK 16: Marks Between 60 and 90")

for student in students.find({
    "marks": {"$gte": 60, "$lte": 90}
}):
    print(student)


# Task 17: Find Computer or IT department students
print("\nTASK 17: Computer or IT Department")

for student in students.find({
    "department": {"$in": ["Computer", "IT"]}
}):
    print(student)


# Task 18: Find students whose age is not equal to 20
print("\nTASK 18: Age Not Equal to 20")

for student in students.find({"age": {"$ne": 20}}):
    print(student)


# Task 19: Sort students by marks in ascending order
print("\nTASK 19: Marks Ascending Order")

for student in students.find().sort("marks", 1):
    print(student)


# Task 20: Sort students by marks in descending order
print("\nTASK 20: Marks Descending Order")

for student in students.find().sort("marks", -1):
    print(student)


# =====================================================
# SECTION D: UPDATE AND DELETE OPERATIONS
# =====================================================

# Task 21: Update Rahul's marks to 85
print("\nTASK 21: Update Rahul's Marks")

result = students.update_one(
    {"name": "Rahul"},
    {"$set": {"marks": 85}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)


# Task 22: Increase Amit's fees by 5000
print("\nTASK 22: Increase Amit's Fees")

result = students.update_one(
    {"name": "Amit"},
    {"$inc": {"fees": 5000}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)


# Task 23: Add email field to one student
print("\nTASK 23: Add Email Field")

student = students.find_one({"name": "Sneha"})

if student:
    result = students.update_one(
        {"_id": student["_id"]},
        {"$set": {"email": "sneha@example.com"}}
    )
    print("Email added successfully")
else:
    print("Sneha not found")


# Task 24: Delete one student named Rohit
print("\nTASK 24: Delete One Rohit Record")

result = students.delete_one({"name": "Rohit"})

print("Deleted records:", result.deleted_count)


# Task 25: Delete students whose marks are less than 35
print("\nTASK 25: Delete Students With Marks Below 35")

result = students.delete_many({
    "marks": {"$lt": 35}
})

print("Deleted records:", result.deleted_count)

# FINAL RESULT

print("\nTotal students remaining:", students.count_documents({}))

print("\nMongoDB Python Assignment Completed!")

client.close()
