import csv


students = []
with open("names.csv") as file:

    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "location": row["location"]})

    # for line in file:
    #     name, location = line.rstrip().split(",")
    #     student = {'name': name, 'location': location}
    #     students.append(student)

# def get_name(student):
#     return student['name']



for student in sorted(students , key= lambda student: student['name']):
    print(f"{student['name']} is from {student['location']}")
