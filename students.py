import csv


students = []
with open("names.csv") as file:

    reader = csv.reader(file)

    # for line in file:
    #     name, location = line.rstrip().split(",")
    #     student = {'name': name, 'location': location}
    #     students.append(student)

# def get_name(student):
#     return student['name']



for student in sorted(students , key= lambda student: student['name']):
    print(f"{student['name']} is from {student['location']}")
