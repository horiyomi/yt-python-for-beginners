
students = [
    {
        "name": "Tom",
        "age": 15,
        "cgpa": 4.0
    },
    {
        "name": "Nick",
        "age": 25,
        "cgpa": 3.2
    },
    {
        "name": "Becky",
        "age": 18,
        "cgpa": 4.6
    },
]



def student_cgpa(students):
    cgpa = []

    for student in students:
        cgpa.append(student["cgpa"])

    return cgpa
