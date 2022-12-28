import sys
# try:
    # print("hello, my name is, ", sys.argv[1]) # when you put in as "python name.py Phebe"
# except IndexError:
#     print("Too few arguements")

#check for errors
if len(sys.argv) < 2:
    sys.exit("too few arg")
# elif(sys.argv) > 2:
#     sys.exit("too many error")

# #Print name tags
# print("hello my name is", sys.argv[1])
for arg in sys.argv[1:]:
    print("hello, my name is", arg)


