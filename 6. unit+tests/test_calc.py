# from calculator import square

# def main():
#     test_square()


# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print ("2 square is not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 square does not equal 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print ("-2 square is not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 square does not equal 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 square does not equal 0")

# if __name__ == "__main__":
#     main()

from calculator import square

def test_positive():
    assert square(2) ==4
    assert square(3) == 9

def test_negative():
    assert square(-2) ==4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0

def test_str():
    # with pytest.raises(TypeError): #pytest doesnt seem to work, find a source
        square("cat")
    
