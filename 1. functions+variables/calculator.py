#x = float(input("what is x? "))
#y = float(input("what is y "))

#float is used for decimals
#int is used for digits
#round is used to round deciomals
# :, is used to seperate numbers excedding 4 digits eg, 4,000
# :.2f is used to specifiy how many numbers it is rounded to
#z = x / y
#print(f"{z:.2f}")
# tưo astricks ráies the pơưer ò the number
# pow raises something to the power  that takes two arguements, the first being the varible eg. n, then the exponenet which can be two 

def main():
    x = int(input("what's x? "))
    print ("x squared is", square(x))

def square(n):
    return n * n

main()