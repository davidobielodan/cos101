# Store and display a student's details in a dictionary.
student = {
"name": "Ada Okeke",
"matric_number": "VUA/001",
"programme": "Software Engineering",
"score": 75
}
print("STUDENT PROFILE")
print("===============")
print(f"Name: {student['name']}")
print(f"Matric number: {student['matric_number']}")
print(f"Programme: {student['programme']}")
print(f"Score: {student['score']}")
student["score"] = 80
print()
print(f"Updated score: {student['score']}")
