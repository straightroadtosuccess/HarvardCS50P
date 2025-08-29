students = ["Hermoine", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)








# students = ["Hermoine", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i+1, students[i])

# students = ["Hermoine", "Harry", "Ron"]

# gryffindors = {student, "Gryffindor" for student in students}

# print(gryffindors)

# students = ["Hermoine", "Harry", "Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# print(gryffindors)


# students = [
#     {"name": "Hermoine", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]


# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"


# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])


# students = [
#     {"name": "Hermoine", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# def is_gryffindor(s):
#     if s["house"] == "Gryffindor":
#         return True
#     else:
#         return False


# students = [
#     {"name": "Hermoine", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# gryffindors = [
#    student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)
