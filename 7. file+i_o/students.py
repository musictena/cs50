# with open("name.csv") as file:
#     for line in file:
#        name, house = line.rstrip().split(",") #name and house are split into two varibles house and name
#        print(f"{name} is in {house}") #  name[0] is in #name[1] is used to seperate the list that is serpeated with a comma
students = []

with open("name.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") #remove space and add a comma
#       student.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)
        student= {"name":name, "house": house} #this a dictionary
        # student["name"] = name  #dictionary keys
        # student["house"] = house name:name is another way to minmize the code
        students.append(student)
#moving onto the the solution to getpython o look at a key insde each dictionary and sort it that way, so we can sort by any field

# def get_name(student): #used to return a name from the dictionary student
#     return student["name"]


#pythn allows you to pass functions as arguements into other functions, getnamefunction is passed into function sorted
#lambda is squivlent to the key getname function, but it essentially is called student and it accesses the student name to
for student in sorted(students, key=get_name): # get_house can also get it to be sorted by alphabetical order in terms of the house list,  reverse=True is to reverse the list from z to a
    print(f"{student['name']} is in {student['house']}")
