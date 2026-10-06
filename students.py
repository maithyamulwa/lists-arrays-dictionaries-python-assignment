# students.py
# Lists, arrays, and dictionaries of students

# 1. LIST of students
students_list = ["Mulwa", "Amina", "Brian", "Cynthia", "David"]

print("LIST OF STUDENTS")
print(students_list)

# Common list operations
students_list.append("Esther")        # add a student
students_list.remove("Brian")         # remove a student
print("First student:", students_list[0])
print("Total students:", len(students_list))
print()

# 2. ARRAY of students
# Python has no built-in array type like other languages, so we use the
# array module, which only holds one data type. Here we store student IDs.
from array import array

student_ids = array("i", [101, 102, 103, 104, 105])

print("ARRAY OF STUDENT IDs")
print(student_ids)

student_ids.append(106)
print("First ID:", student_ids[0])
print("Total IDs:", len(student_ids))
print()

# 3. DICTIONARY of students
# Keys are student IDs, values are student details
students_dict = {
    101: {"name": "Mulwa", "age": 22, "grade": "A"},
    102: {"name": "Amina", "age": 21, "grade": "B"},
    103: {"name": "Brian", "age": 23, "grade": "A"},
}

print("DICTIONARY OF STUDENTS")
for student_id, details in students_dict.items():
    print(student_id, "->", details["name"], "| Age:", details["age"], "| Grade:", details["grade"])

# Add and update entries
students_dict[104] = {"name": "Cynthia", "age": 22, "grade": "C"}
students_dict[102]["grade"] = "A"
print("Student 102:", students_dict[102])
