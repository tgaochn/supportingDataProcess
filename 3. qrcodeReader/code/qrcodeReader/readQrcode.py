# !/usr/bin/env python
# coding: utf-8
"""
readQrcode.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    2018-7-5 13:08:29
Link:

Description:

"""

import os
from PIL import Image
import math


def func():
    X = 606
    Y = 4409
    W = 277
    H = 226
    inputFn = r'C:\Users\Administrator\Desktop\today\card2\DCIM\100MSDCF\C2_02321.JPG'
    outputFn = r'data/tmp.png'
    croppedImgFn = cropImg(inputFn, outputFn, X, Y, W, H)
# end_func


def cropImg(inputFn, outputFn, x, y, w, h):
    im = Image.open(inputFn)
    region = im.crop((x, y, x + w, y + h))
    region.save(outputFn)
    return outputFn
# end_func

def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
