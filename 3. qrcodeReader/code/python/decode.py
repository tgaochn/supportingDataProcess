# !/usr/bin/env python
# coding: utf-8
"""
decode.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    2018-7-1 00:18:23
Link:
    
Description:
    
"""
import qrtools

def func():
    qr = qrtools.QR()
    # qr.decode("data/01.jpg")
    # qr.decode("data/test_qr1.png")
    qr.decode("image.jpg")
    print qr.data
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
