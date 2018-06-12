from PIL import Image, ImageColor
im = Image.open('/Users/xieyanduo/Desktop/pythonBird/Lenna.jpg')
#im.getrgb(50, 50, 50)
#print(im.getpixel(0, 0))
#im.save('pig.png')
#print(im.width)
#im.rgb('30','30','30')
#a = [0.5, 0.5, 0.5] 
#im2 = im.new('RGB', (200, 200), (50, 50, 50))
for i in range(im.width):
    for j in range(im.height):
        pxl = im.getpixel((i, j))
        r, g, b = pxl
        im.putpixel((i, j), (int(r*0.5), int(g*0.5), int(b*0.5)))
       # print(r, g, b)
im.show()



