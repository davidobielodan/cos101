# Add three student names to a list.
students = []
for number in range(1, 4):
    student_name = input(f"Enter name of student {number}: ")
    students.append(student_name)
print()
print("Registered students:")
for student in students:
    print(student)