def main():
    hello("world")
    goodbye("goodbye")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__": #since there is a conditional here that can only be used if something is typed in by the user in ther terminal
    main()
