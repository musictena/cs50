# parity = mathmatical way to refer if a number is even or odd

# x = int(input("what is x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(input("what is x? "))
    if is_even (x):
        print("Even")
    else: 
        print("odd")

def is_even(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
    # return True if num % 2 == 0 else False
    
    return num %  2 == 0 

   

main()
