import pyqrcode as code
text=code.create('my name is giri')
text.png('D:\\giriqr.png',scale=5)
text.svg('D:\\giriqr.svg',scale=8)