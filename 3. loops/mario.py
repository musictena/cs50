# def  main():
#     print_column(3)


# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()

#making a row vertical
# def main():
#     print_row(4)

# def print_row(width):
#     print("?"* width)

# main()

# making a square
def main():
    print_square(3)
# for each row in square
def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        # for j in range(size):
        #     #print brick
        #     print("#", end="")
       
        print_row(size)
        #print the bricks in one row
        #print()
def print_row(width):
     print("#" * width)  
main()
