# !/usr/bin/env python
# coding: utf-8
"""
qrcode_test.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    2018-7-1 00:12:25
Link:
    
Description:
    
"""
# Import QR Code library
import qrcode


def func():
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # The data that you want to store
    data = "The Data that you need to store in the QR Code"

    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("image.jpg")
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
