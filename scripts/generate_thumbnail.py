import os
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--folder_path', type=str, help='folder with images which need a thumbnail', required=True)
args = parser.parse_args()
folder_path = args.folder_path + "/"

print("Observed this: " + folder_path)

size = [512, 512]

def get_thumbnail(folder, filename, box, fit=True):
    img = Image.open(folder + filename)
    if img:
        # preresize image with factor 2, 4, 8 and fast algorithm
        factor = 1
        while img.size[0] / factor > 2 * box[0] and img.size[1] * 2 / factor > 2 * box[1]:
            factor *= 2
        if factor > 1:
            img.thumbnail((img.size[0] / factor, img.size[1] / factor), Image.NEAREST)

        # calculate the cropping box and get the cropped part
        if fit:
            x1 = y1 = 0
            x2, y2 = img.size
            wRatio = 1.0 * x2 / box[0]
            hRatio = 1.0 * y2 / box[1]
            if hRatio > wRatio:
                y1 = int(y2 / 2 - box[1] * wRatio / 2)
                y2 = int(y2 / 2 + box[1] * wRatio / 2)
            else:
                x1 = int(x2 / 2 - box[0] * hRatio / 2)
                x2 = int(x2 / 2 + box[0] * hRatio / 2)
            img = img.crop((x1, y1, x2, y2))

        # Resize the image with best quality algorithm ANTI-ALIAS
        img.thumbnail(box, Image.ANTIALIAS)
        output = folder + filename + "_thumbnail.jpg"
        img.save(output, "JPEG")
        return output

for infile in os.listdir(folder_path):
    print("Removing old thumbnail entries")
    if "thumbnail" in infile:
        print("Removing " + infile)
        os.remove(folder_path + infile)

for infile in os.listdir(folder_path):
    print(folder_path + infile)
    try:
        print(get_thumbnail(folder_path, infile, (512, 512)))
    except:
        print("Could not open " + infile)