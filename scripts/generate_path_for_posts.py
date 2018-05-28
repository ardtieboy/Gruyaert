import os
from PIL import Image

folder = "bekledingen/keukens"
input_dir = '/Users/ardscheirlynck/Documents/Websites/gruyaert/images/'+folder+'/'

print("sub_images:")
for infile in os.listdir(input_dir):
    if "thumbnail" not in infile and "DS_Store" not in infile:
        print("  - path: \"" + "/images/" + folder +"/" + infile + "\"")