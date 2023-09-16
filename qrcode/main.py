import qrcode

data = "https://g-101.github.io/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="#b0e0e6")
image.save("images/portfolio.png")
image.show()