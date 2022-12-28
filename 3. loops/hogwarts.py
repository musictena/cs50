#lists
#students = ["bob", "fish", "cat"]

#
# print(students[0])
# print(students[1])
# print(students[2])
# len is used to idenitify the lengh of a list
#for loop
# for s in range(len(students)):
#     print (s +1, students[s])

# houses = ["griffen", "slytherin"]

# #asscoiating tweo lists with each other
# #dict aka dictionary is used to associate things with things
# students = {
#     "Bob":"Griffen", 
#     "cat":"pet", 
#     "dog": "pet"
#     }
# # print(students["Bob"])#for dict you use the name
# for student in students: #when you use a for loop in dict, it initaties over the first variable
#     print(student, students[student], sep = ", ")


students = [
    {"name": "bob", "house":"griffen", "patronis":"Otter"},
    {"name": "Bill", "house": "griffen", "patronis": None},
    {"name": "Lep", "house": "Gri", "patronis": "Pet"}
]

for student in students:
    print(student["name"], student["house"], student["patronis"], sep =", ") #finding keys in lists