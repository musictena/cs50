import csv


# students = []
# with open("students.csv") as file:
#     reader = csv.reader(file) #read is used to read a csv is and where all the commas, corner casese etc.
#     for row in reader:
#         students.append({"name": row["name"], "home":row["home"]}) #give the varible name for each row

# for student in sorted(students, key=lambda student: student["name"]): # get_house can also get it to be sorted by alphabetical order in terms of the house list,  reverse=True is to reverse the list from z to a
#     print(f"{student['name']} is in {student['home']}")
# ----------------------------------------------------

name = input("what's yourname? ")
home = input("what's your home? ")

with open("students.csv", "a") as file: #a is append mode
    writer = csv.DictWriter(file, fieldnames=["name","home"]) #fieldname is used to read the csv file in the order that they are in
    writer.writerow(["name":name,"home":home])
