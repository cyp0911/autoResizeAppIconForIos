import os, sys
import PIL
from PIL import Image
from resizeimage import resizeimage


sizeName = ['AppStoreIOS', 'IpadPro', 'Ipad@2x', 'Ipad', 'IpadSpotLight', 'IpadSpotLight@2x', 'IpadSetting', 'IpadSetting@2x', 'IpadNotification', 'IpadNotification@2x', 'IphoneApp@2x', 'IphoneApp@3x', 'IphoneSpot@2x', 'IphoneSpot@3x', 'Iphone@2x', 'Iphone@3x', 'IphoneNotification@2x', 'IphoneNotification@3x']

size = [1024, 167, 76*2, 76, 40, 80, 29, 29*2, 20, 20*2, 60*2, 60*3, 40*2, 40*3, 29*2, 29*3, 20*2, 20*3]

if __name__ == "__main__":
    with open('itunesIcon.png', 'r+b') as f:
        with Image.open(f) as image:
            for index in range(len(sizeName)):
                cover = resizeimage.resize_cover(image, [size[index], size[index]])
                cover.save('%s.png' % sizeName[index], image.format)
