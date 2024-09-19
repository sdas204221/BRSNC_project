from scramble import catMap
from encryption import e1
from PIL import Image

inputPath="../data/images/"
outputPath="../data/output/"
imageName="4.1.04.tiff"
def main(size,L):
    img=Image.open(inputPath+imageName)
    grayImg=img.convert("L")
    grayImg.save(outputPath+"scramble/0.png")
    grayPixels=grayImg.load()
    oldPixels=grayPixels
    newImg=Image.new("L",(size,size),(0))
    newPixels=newImg.load()
    z=0
    while(z<L):
        z=z+1
        for i in range(size):
            for j in range(size):
                x,y=catMap(i,j,size)
                newPixels[x,y]=oldPixels[i,j]
        if z==91:
            encryptedImage=e1(newPixels,size,0.5,3.14)
            encryptedImage.save(outputPath+str(z)+".encrypted.png")
            pass
        path=outputPath+"scramble/"+str(z)+".png"
        newImg.save(path)
        if(z%10==0):
            print("Image saved "+path)
        oldImg=Image.open(path)
        oldPixels=oldImg.load()

main(256,192)
