from PIL import Image
# mac = Image.open('example.jpg')
# # mac.show()
# print(mac.size)
# print(mac.format)
# print(mac.filename)
#
# cropped1 = mac.crop((0, 0, 100, 100))
# cropped1.show()

pencils = Image.open('pencils.jpg')
w, h = pencils.size
# pencils.show()
# print(pencils.size[0])
cropped2 = pencils.crop((0, 1100, w/3, h))
cropped2.putalpha(10)
cropped2.show()