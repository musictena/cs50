import sys #sys library is used to access those command line arguements

from PIL import Image # a pillow library i sused to treat those files as images and with all the functionality that comes with that library

images  = []#the images list just to accumlate al of these images, one at a time from the command-line

#a loop iterates over all images and add them to this list ater opening them with the library
for arg in sys.argv[1:]:
    image- Image.open(arg)
    images.append(image)

images[0].save("costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0)
#save the first image but the library appends the other image to itas well. this being bracket[1], it is paused for 200 milliseconds and i is repeated indefinitly 
