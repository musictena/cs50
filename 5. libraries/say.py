# import cowsay
import sys

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1]) # when you type your name in thee terminal after the name of the cow

from saying import hello #import from another file called saying.py

if len(sys.argv) == 2: 
    hello(sys.argv[1])