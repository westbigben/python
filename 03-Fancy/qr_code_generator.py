# Generate a QR code for a given URL or text
import qrcode

data = "https://github.com/yourusername"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr_code.png")
print("QR code saved as my_qr_code.png")