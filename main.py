#with open('photo.jpeg', 'ab') as f: #Open the jpg file then append bytes as you do not want to overwrite the file.
#    f.write(b"Hello World")
"""
with open('photo.jpeg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)
    print(f.read())


import PIL.Image
import io

img = PIL.Image.open('hiddenimage.jpeg')
byte_arr = io.BytesIO()
img.save(byte_arr, format='JPEG')

with open('photo.jpeg', 'ab') as f:
    f.write(byte_arr.getvalue())


with open('photo-hiddenphoto.jpeg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)

    new_img = PIL.Image.open(io.BytesIO(f.read()))
    new_img.save("new_image.png")
"""