import qrcode

input = "https://www.olimpica.com/?gclid=CjwKCAjwtKmaBhBMEiwAyINuwPOZhTGkIstM62ORuuWNH1RWWJOHH40c555L3szpMEFRmZ5cktdzchoCnbEQAvD_BwE"
qr = qrcode.QRCode(version=1,border=5)

qr.add_data(input)
qr.make(fit=True)

img = qr.make_image(fill="black",back_color="white")
img.save("QR_super.png")


