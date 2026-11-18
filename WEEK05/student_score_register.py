# Collect, display, summarise, and search student scores.
students = []
student_count = int(input("How many students? "))
if student_count <= 0:
    print("The number of students must be greater than zero.")
else:
    # Collect student records.
    for number in range(1, student_count + 1):
        print()
        print(f"STUDENT {number}")

        name = input("Enter student name: ").strip()
        score = float(input("Enter score from 0 to 100: "))
        while score < 0 or score > 100:
            print("Invalid score. Enter a value from 0 to 100.")
            score = float(input("Enter score: "))
        student = {
            "name": name,
            "score": score
            }
        students.append(student)
    # Display each stored record.
    print("")
    print("STUDENT SCORE REGISTER")
    print("======================")

    for student in students:
        print(f"{student['name']}: {student['score']:.2f}")
    # Calculate the class summary.
    total = 0.0
    highest = students[0]["score"]
    lowest = students[0]["score"]

    for student in students:
        score = student["score"]
        total += score

        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    average = total / len(students)

    print()
    print("CLASS SUMMARY")
    print("=============")
    print(f"Number of students: {len(students)}")
    print(f"Total score: {total:.2f}")
    print(f"Average score: {average:.2f}")
    print(f"Highest score: {highest:.2f}")
    print(f"Lowest score: {lowest:.2f}")

    # Search for every record whose name matches.
    print()
    search_name = input("Enter a student name to search: ").strip()

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print(
                f"Match: {student['name']} — "
                f"Score: {student['score']:.2f}"
            )
            found = True

    if not found:
        print("Student not found.")
