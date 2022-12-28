
#while loops

# counting down
# i = 3
# while i != 0:
#     print("Meow")
#     i = i -1

# counting up from 1
# i = 1
# while i <= 0:
#     print("Meow")
#     i += 1 #equivelnet to ++

# lists loop equivlent to for loop
# for i in [0,1,2]:
# for _ in range(3): #function called range
#     print("Meow")

# multiplying
# print("Meow\n" * 3, end="")


# meowing several times
# while True:
#     number = int(input("what's number of times it meows? "))
#     if number > 0:
#         break
# for _ in range (number):
#     print("Meow")

#example 2
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what's number of times it meows? "))
        if n > 0:
         return n
def meow(n):
    for _ in range(n):
        print("meow")

main()