from tkinter import Scale
import png
from tkinter import Scale
import pyqrcode
from PIL import Image
link = input("Enter the link to convert it to QR code : ")
qr_code = pyqrcode.create(link)
qr_code.png ("QRCode.png", scale=5)
Image.open = ("QRCode.png")