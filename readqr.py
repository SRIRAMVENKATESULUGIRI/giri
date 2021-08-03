from pyzbar.pyzbar import decode
from PIL import Image
content=decode(Image.open('blogqr.jpg'))
print(content[0].data.decode('ascii'))

