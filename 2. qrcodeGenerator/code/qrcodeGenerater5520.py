# !/usr/bin/env python
# coding: utf-8
"""
qrcodeGenerater.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    2018-7-1 02:05:33
Link:
    
Description:
    
"""

import qrcode
import os
from PIL import Image
import math


QRCODE_OUTPUT = r'D:\qrcode'
TEX_FN = r'D:\Dropbox\project\4. visualization\3. supporting data process\2. qrcodeGenerator\data\latex\qrcode.tex'

LABEL_LIS = [
    '1-1',
    '1-2',
    '1-3',
    '2-1',
    '2-2',
    '2-3',
    '3-1',
    '3-2',
    '3-3',
    '4-2',
    '4-3',
]


# region of qrcode for cropping
X = 38
Y = 38
W = 215
H = 215

def func():
    labelLis = LABEL_LIS
    imgFnLis = []

    texFolder = os.path.dirname(TEX_FN)
    if not os.path.exists(texFolder):
        os.makedirs(texFolder)
    if not os.path.exists(QRCODE_OUTPUT):
        os.makedirs(QRCODE_OUTPUT)

    for label in labelLis:
        imgFn = '%s/%s.jpg' % (QRCODE_OUTPUT, label)

        # Create qr code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        # Add data
        qr.add_data(label)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image()

        # Save it somewhere, change the extension as needed:
        img.save(imgFn)

        # crop qrcode
        croppedImgFn = cropImg(label, X, Y, W, H)
        imgFnLis.append(croppedImgFn)

        os.remove(imgFn)
    # end_for

    writeTex(TEX_FN, labelLis, imgFnLis)
# end_func


def cropImg(label, x, y, w, h):
    inputFn = '%s/%s.jpg' % (QRCODE_OUTPUT, label)
    outputFn = '%s/%s.png' % (QRCODE_OUTPUT, label)
    im = Image.open(inputFn)
    region = im.crop((x, y, x + w, y + h))
    region.save(outputFn)
    return outputFn
# end_func


def writeTex(texFn, labelLis, imgFnLis):
    header = ('\\documentclass[letterpaper]{article}\n'
              '\\usepackage[english]{babel}\n'
              '\\usepackage[utf8]{inputenc}\n'
              '\\usepackage{graphicx}\n'
              '\\usepackage{geometry}\n'
              '\\usepackage{graphics}\n'
              '\\usepackage{caption}\n'
              '\\usepackage{geometry}\n'
              '\\usepackage{tcolorbox}\n'

              '\\geometry{letterpaper, left = 0.475cm, right = 0.475cm, top = 1.272cm, bottom = 1.3013cm}\n'

              '\\begin{document}\n'
              '\\begin{figure}[htbp]\n')

    tail = ('\\end{figure}\n'
            '\\end{document}\n')

    newPageStr = ('\\end{figure}\n'
                  '\\begin{figure}[htbp]\n')

    with open(texFn, 'w') as texFile:
        texFile.write(header)
        pageCnt = int(math.ceil(len(labelLis) / 30.0))
        labelCnt = len(labelLis)
        for i in xrange(pageCnt * 30):
            if i < labelCnt:
                label = labelLis[i]
                imgFn = imgFnLis[i].replace('\\', '/')
                imgStr = ('\\begin{minipage}[htbp]{0.333333\\textwidth}\n'
                        '\\begin{tcolorbox}[boxrule = 0.2mm, width=6.67428cm, colback=white, left=5mm, top=-0.5mm, bottom=-0.5mm]\n'
                        '\\begin{minipage}{0.45\\textwidth}\n'
                        '\\includegraphics[width=2.4023cm]{%s}\n'
                        '\\end{minipage}\n'
                        '\\begin{minipage}{0.1\\textwidth}\n'
                        '\\includegraphics[width=0cm]{%s}\n'
                        '\\renewcommand{\\captionfont}{\\Large \\bfseries}\n'
                        '\\caption*{\\rotatebox{90}{%s}}\n'
                        '\\end{minipage}\n'
                        '\\end{tcolorbox}\n'
                        '\\end{minipage}\n' % (imgFn, imgFn, label.replace('_', '\\_')))
            if i % 3 == 0 and i > 0:
                texFile.write('\n\\setlength{\\parskip}{-1.42165mm}\n\n')
            if i % 30 == 0 and i > 0:
                texFile.write(newPageStr)
            texFile.write(imgStr)
        texFile.write(tail)
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
