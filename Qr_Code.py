# From tkinter import. Scale
from tkinter import Scale
# import png
import png
# Import pyqrcode.
import pyqrcode
# Deserialize from PIL import image
from PIL import Image
# Enter the link to convert it to QR code
link = input("Enter the link to convert it to QR code : ")
# Create a qrcode link.
qr_code = pyqrcode.create(link)
# QRCode. png QRCode
qr_code.png ("QRCode.png", scale=5)
# QRCode. png
Image.open = ("QRCode.png")
