student_record = {}

name = input("Enter your name:")
student_record['Name'] = name

age = int(input("\nEnter your age:"))
student_record['Age'] = age

subject = input("\nEnter your favorite subject:")
student_record['Subject'] = subject

print("\nStudent Record:\n")
for key, value in student_record.items():
    print(f"{key}: {value}")