names = []

with open('names.txt', 'r') as file:
    # lines = file.readlines()

    for line in file:
        names.append(line.rstrip())


for line in sorted(names , reverse= True):
    print(line)
