# -*- coding: utf-8 -*-

import sys
import math
from PIL import Image

if __name__ == "__main__":
    param = sys.argv
    size = int(param[1])
    src_path = param[2]
    dst_path = param[3]

    canvas = Image.new('RGB', (size, size), (255, 255, 255))
    src_image = Image.open(src_path, 'r')
    
    if src_image.width >= src_image.height:
        if src_image.width >= size:
            src_image.thumbnail((size, int(src_image.height * size / src_image.width)), Image.ANTIALIAS)
        else:
            src_image = src_image.resize((size, int(src_image.height * size / src_image.width)))

        #print src_image.width, src_image.height
        for i in range(0, int(size / src_image.height) + 1):
            canvas.paste(src_image, (0, src_image.height * i))
    else:
        if src_image.height >= size:
            src_image.thumbnail((int(src_image.width * size / src_image.height), size), Image.ANTIALIAS)
        else:
            src_image = src_image.resize((int(src_image.width * size / src_image.height), size))

        #print src_image.width, src_image.height
        for i in range(0, int(size / src_image.width) + 1):
            canvas.paste(src_image, (src_image.width * i, 0))

    #print("dst_path:", dst_path)
    canvas.save(dst_path, 'JPEG', quality=100, optimize=True)
    print("src_path:", src_path)
