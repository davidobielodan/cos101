# Remove spaces around a name and display different versions.
student_name = input("Enter your full name: ")
clean_name = student_name.strip()
print(f"Original: '{student_name}'")
print(f"Without surrounding spaces: '{clean_name}'")
print(f"Uppercase: {clean_name.upper()}")
print(f"Lowercase: {clean_name.lower()}")
print(f"Title case: {clean_name.title()}")
