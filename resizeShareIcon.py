import os, sys
import PIL
from PIL import Image
from resizeimage import resizeimage


Name = []
size = [57, 57*2, 57*3]
Icon = sys.argv[1]
for i in range(3):
    if (i == 0):
        Name.append(Icon) 
    elif (i == 1):
        newIcon = Icon + '@2x'
        Name.append(newIcon)
    elif (i == 2):
        newIcon = Icon + '@3x'
        Name.append(newIcon)
print(Name)

if __name__ == "__main__":
    with open('%s-native.png' % Icon, 'r+b') as f:
        with Image.open(f) as image:
            for index in range(len(Name)):
                cover = resizeimage.resize_cover(image, [size[index], size[index]])
                cover.save('%s.png' % Name[index], image.format)

