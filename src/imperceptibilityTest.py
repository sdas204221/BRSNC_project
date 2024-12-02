import math
from PIL import Image

def MSE(img1,img2): #mean square error
    pixels1=img1.load()
    pixels2=img2.load()
    if(img1.size!=img2.size):
        print("image dimensions did not match")
        return
    x,y=img1.size
    sum=0
    for i in range(x):
        for j in range(y):
            sum+=(pixels1[i,j]-pixels2[i,j])**2
    return sum/(x*y)

def PSNR(img1,img2): #peak signal-to-noise ratio
    return 10*math.log10(255*255/MSE(img1,img2))


def test():
    img1=Image.open("../data/output/scramble/0.png")
    img2=Image.open("../data/output/90.encrypted.png")
    psnr=PSNR(img1,img2)
    print(psnr)
