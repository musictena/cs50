
def main():
    student = get_student()
    #tuple
    # if student[0] == "padma":
    #     student[1] = "Ravenclaw"

    #dict
    if student["name"] == "padma":
        student["house"] = "Ravenclaw"
    print (f"{student['name']} from {student['house']}")

# def get_name():
#     return input("name: ")

# def get_house():
#     return input("house: ")

def get_student():
    #this is a tuple
    # name = input("name: ")
    # house =  input("house: ")
    # return [name, house] #used to return two values

    #this is a dict
    name = input("name: ")
    house = input("house: ")
    return {"name": name, "house": house}

if __name__ == "__main__": #by using __main__ is becomes part of a modeule/libary
    main()