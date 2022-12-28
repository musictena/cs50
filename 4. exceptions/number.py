#value error = is an error that occurs because the string or input is not expected 
#name error = is an error, an error in your code
#literal is the thing that has been typed in
#if you want to find exception you can use the word 'try'  and 'except' to find errors
#

def main():
    x = get_int("what's x") #passese a prompt when function is called
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try: #try statement
            return int(input(prompt)) #for try you should only use one statement 
        except ValueError:
            # print("x is not an integer")
            pass #pass is used to handling errors by bypassing the error and returning to the try statement
        # else:
        #     return(x)




main()