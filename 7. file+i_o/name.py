# name = []

# for _ in range(3):
#     name.append(input("what's your name? "))
    

# for names in sorted(name): #sorts the info in alphabetic order
#     print(f"hello, {names}")

name = input("what's your name? ")

file = open("name.txt", "w") 
#w =write, the write function is used to change the content of the file or create a new file
#  since open returns a file handle, to a special value that allows me to access the file subsquently

file.write(name)
file.close()

#since the external text was not appended the text was replaced each time


