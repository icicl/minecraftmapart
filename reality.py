white = [220, 220, 220]
orange = [186, 109, 44]
magenta = [153, 65, 186]
lt_blue = [88, 132, 186]
yellow = [197, 197, 44]
lime = [109, 176, 21]
pink = [208, 109, 142]
gray = [65, 65, 65]
lt_gray = [132, 132, 132]
cyan = [65, 109,132]
purple = [109, 54, 153]
blue = [44, 65, 153]
brown = [88, 65, 44]
green = [88, 109, 44]
red = [132, 44, 44]
black = [21, 21, 21]

colors = {'white' : [220, 220, 220],
'orange' : [186, 109, 44],
'magenta' : [153, 65, 186],
'lt_blue' : [88, 132, 186],
'yellow' : [197, 197, 44],
'lime' : [109, 176, 21],
'pink' : [208, 109, 142],
'gray' : [65, 65, 65],
'lt_gray' : [132, 132, 132],
'cyan' : [65, 109,132],
'purple' : [109, 54, 153],
'blue' : [44, 65, 153],
'brown' : [88, 65, 44],
'green' : [88, 109, 44],
'red' : [132, 44, 44],
'black' : [21, 21, 21]
}



"""
black = [25,25,25]
green = [102,127,51]
lt_blue = [102,153,216]
brown = [102,76,51]
lt_gray = [108,108,108]
red = [108,36,36]
lime = [109,176,21]
purple = [109,54,153]
orange = [114,67,27]
yellow = [121,121,27]
magenta = [125,53,152]

"""
import os
def closest(pix):
    min_ = 256*256*3
    min_pix = [255]*3
    for i in colors:
        dist = (pix[0]-colors[i][0])**2+(pix[1]-colors[i][1])**2+(pix[2]-colors[i][2])**2
        if dist < min_:
            min_=dist
            min_pix = colors[i]
    return tuple(min_pix)

from PIM import Image
size = 64,64
for i in os.listdir("./in"):
    try:
        b = Image.open("./in/"+i)
    except:
        print(i + " is mega gay")
    b=b.crop((0,0,min(b.height,b.width),min(b.height,b.width)))
    b.thumbnail(size)
    p = b.load()


    for x in range(b.width):
        for y in range(b.height):
            p[x,y] = closest(p[x,y])

#    b.show()
    b.save(i[:-4]+"_"+str(size[0])+"x"+str(size[1])+".png","png")
    for x in range(0,b.width,16):
        for y in range(b.height):
            p[x,y] = (0,0,0)
    for x in range(b.width):
        for y in range(0,b.height,16):
            p[x,y] = (0,0,0)
    b.save(i[:-4]+"_"+str(size[0])+"x"+str(size[1])+"_with_guidelines.png","png")
    for x in range(0,b.width,4):
        for y in range(b.height):
            p[x,y] = (77,77,77)
    for x in range(b.width):
        for y in range(0,b.height,4):
            p[x,y] = (77,77,77)
    for x in range(0,b.width,16):
        for y in range(b.height):
            p[x,y] = (0,0,0)
    for x in range(b.width):
        for y in range(0,b.height,16):
            p[x,y] = (0,0,0)
    b.save(i[:-4]+"_"+str(size[0])+"x"+str(size[1])+"_with_fine_guidelines.png","png")

