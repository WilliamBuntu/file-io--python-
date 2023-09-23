import csv

name = input('what is your name ')
home = input('what is your home address ')

with open("locals.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames= ["name", "home"])
    writer.writerow({"name": name, "home": home})
