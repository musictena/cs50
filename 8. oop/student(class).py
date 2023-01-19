class Student:
    def __init__(self, name, house): #this is a instance method
        if not name:
            raise ValueError("Missing name")
        if house not in("griffen", "huffle", "Raven"):
            raise ValueError("Invalid House")
        self.name = name #initialises the variables
        self.house = house


def main():
    student = get_student()
    print (f"{student.name} from {student.house}")
def get_student():
    student = Student() #create an object of a class
    # student.name = input("Name: ") #attributes/objects
    # student.house = input("house: ")
    name =input("Name: ")
    house = input("house: ")
    return Student(name,house) #constructor call



if __name__ == "__main__": #by using __main__ is becomes part of a modeule/libary
    main()