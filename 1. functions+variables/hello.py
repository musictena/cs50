#ask what the user is doing
#x = input ("what is your name? ").strip().title()

#saying hello to the user based on their response
"""this is a multi line comment"""
#print("hello,", end="") 
#print(x) #this was to print a variable
#print ("hello", x, sep="blah") #sep is the speration of the varibles or other parameters within a function hence this would output helloblah'x' , since there is no space (default is space)

#print ("hello, \"friend\"") #the two slahes are called escaping and are used to tell the computer that the quotes are not end/start of string but are actual quotes prints "hello "friend""

#print (f"hello, {x}") #f string 

#removes the whitespace of the str
#x = x.strip()

#capatalising the user name ( first name)
#x = x.capitalize()

#captalising the user
#x = x.title()

#split user's nmame into first name and last name
#first, last = x.split(" ") # in print comment, it should only spcifiy one cariable
#print (f"hello, {first}")


#to create a new function

#def is used to define, it should be at the top, to contest it define main() function then def hello function with paramerter

def main():
    name = input("what is ur name ")
    hello(name)             #since it pases the parameter of the name in the function hello

def hello(to="world"):      #the function must also pass a paramaeter in this case to, the world is used only when there is nothing listed in the hello function eg. hello()
    print(f"hello, {to}")

main()
#print(name)

