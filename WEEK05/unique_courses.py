# Identify unique course codes.
registered_courses = [
"COS101",
"MTH101",
"COS101",
"ENG101",
"MTH101"
]
unique_courses = set(registered_courses)
print("Number of course entries:", len(registered_courses))
print("Number of unique courses:", len(unique_courses))
if "COS101" in unique_courses:
    print("COS101 is included.")