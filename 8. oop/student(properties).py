class Student:
    def __init__(self, name, house): #this is a instance method
        if not name:
            raise ValueError("Missing name")
        if house not in["griffen", "huffle", "Raven"]:
            raise ValueError("Invalid House")
        self.name = name #initialises the variables
        self.house = house
        # self.patronus = patronus
    def __str__(self): #always takes one arguement
        return f"{self.name} from {self.house}"
    # def charm(self):
    #     # match self.patronus:
    #         if self.patronus == "Stag":
    #             return ":)"
    #         elif self.patronus =="Otter":
    #             return ":("
    #         elif self.patronus =="dog":
    #             return ":()"
    #         else:
    #             return "meow"

    #getter
    @property
    def _house(self):
        return self._house
    #setter
    @house.setter
    def _house(self.house):
        if house not in ("griffen", "huffle", "Raven"): #error checking for those who rewrites code in main
            raise ValueError("Invalid house")
        self._house = house #_house becuas the instance varibale will get mixed up with house hence _house

def main():
    student = get_student()
    # print (f"{student.name} from {student.house}")
    print(student)
    # print("Expecto Patronum")
    # print(student.charm())
def get_student():
   # student = Student() #create an object of a class
    # student.name = input("Name: ") #attributes/objects
    # student.house = input("house: ")
    name =input("Name: ")
    house = input("house: ")
    # patronus= input("Patronus: ")
    return Student(name,house) #constructor call


if __name__ == "__main__": #by using __main__ is becomes part of a modeule/libary
    main()