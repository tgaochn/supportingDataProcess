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

# NOTE: not for 3_rotatingCamera
QRCODE_OUTPUT = r'D:\qrcode'
TEX_FN = r'D:\Dropbox\project\4. visualization\3. supporting data process\2. qrcodeGenerator\data\latex\qrcode.tex'

LABEL_LIS = [
    '323_1',
    '323_2',
    '323_3',
    '323_4',
    '323_5',
    '323_6',
    '269_4',
    '269_5',
    '220_2',
    '220_3',
    '269_1',
    '220_1',
    '220_4',
    '269_2',
    '220_5',
    '233_2',
    '233_3',
    '240_1',
    '233_1',
    '278_1',
    '278_2',
    '278_3',
    '221_1',
    '222_5',
    '278_4',
    '183_6',
    '240_2',
    '240_4',
    '221_2',
    '221_4',
    '221_6',
    '222_2',
    '240_5',
    '240_3',
    '240_6',
    '221_3',
    '221_5',
    '222_1',
    '222_4',
    '222_6',
    '278_6',
    '183_2',
    '183_4',
    '279_2',
    '279_4',
    '222_3',
    '278_5',
    '183_1',
    '105_1',
    '105_5',
    '220_6',
    '223_2',
    '276_6',
    '105_6',
    '105_4',
    '052_4',
    '233_4',
    '183_3',
    '279_3',
    '105_3',
    '052_5',
    '223_1',
    '223_3',
    '105_2',
    '052_3',
    '279_1',
    '246_2',
    '052_2',
    '317_6',
    '341_6',
    '052_6',
    '317_5',
    '246_3',
    '052_1',
    '279_5',
    '296_6',
    '233_6',
    '296_5',
    '233_5',
    '341_5',
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

              '\\geometry{letterpaper, left = 0.3943cm, right = 0.3943cm, top = 1.272cm, bottom = 1.3013cm}\n'

              '\\begin{document}\n'
              '\\begin{figure}[htbp]\n')

    tail = ('\\end{figure}\n'
            '\\end{document}\n')

    newPageStr = ('\\end{figure}\n'
                  '\\begin{figure}[htbp]\n')

    with open(texFn, 'w') as texFile:
        texFile.write(header)
        pageCnt = int(math.ceil(len(labelLis) / 10.0))
        labelCnt = len(labelLis)
        for i in xrange(pageCnt * 10):
            if i < labelCnt:
                label = labelLis[i]
                imgFn = imgFnLis[i].replace('\\', '/')
                imgStr = ('\\begin{minipage}[htbp]{0.507\\textwidth}\n'
                        '\\begin{tcolorbox}[boxrule = 0.2mm, width=10.192cm, colback=white, left=5mm, top=-0.5mm, bottom=-0.5mm]\n'
                        '\\begin{minipage}{0.6\\textwidth}\n'
                        '\\includegraphics[width=4.94333cm]{%s}\n'
                        '\\end{minipage}\n'
                        '\\begin{minipage}{0.3\\textwidth}\n'
                        '\\includegraphics[width=0cm]{%s}\n'
                        '\\renewcommand{\\captionfont}{\\Huge \\bfseries}\n'
                        '\\caption*{\\rotatebox{90}{%s}}\n'
                        '\\end{minipage}\n'
                        '\\end{tcolorbox}\n'
                        '\\end{minipage}\n' % (imgFn, imgFn, label.replace('_', '\\_')))
            if i % 2 == 0 and i > 0:
                texFile.write('\n\\setlength{\\parskip}{-1.42165mm}\n\n')
            if i % 10 == 0 and i > 0:
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
