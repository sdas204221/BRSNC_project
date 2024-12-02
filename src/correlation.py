from PIL import Image
import statistics

from matplotlib import pyplot as plt

def correlation(x,y):
    n=len(x)
    xMean=statistics.mean(x)
    yMean=statistics.mean(y)
    cov=0
    for i in range(n):
        cov=cov+(x[i]-xMean)*(y[i]-yMean)
    cov=cov/n
    return cov/(statistics.stdev(x)*statistics.stdev(y))

def selfCorrelationHorisontal(image,requirePlot=True):
    grayImg = image.convert("L")
    pixel_values = list(grayImg.getdata())
    x=list(pixel_values[:len(pixel_values)-1])
    y=list(pixel_values[1:len(pixel_values)])
    if(requirePlot):
        scatterPlot(x,y)
    return correlation(x,y)

def selfCorrelationVertical(image,requirePlot=True):
    grayImg = image.convert("L")
    img=grayImg.load()
    sizeX, sizeY=grayImg.size
    pixel_values=list()
    for i in range(sizeY):
        for j in range(sizeX):
            pixel_values.append(img[j,i])    
    x=list(pixel_values[:len(pixel_values)-1])
    y=list(pixel_values[1:len(pixel_values)])
    if(requirePlot):
        scatterPlot(x,y)
    return correlation(x,y)

def toImageCorrelation(image1,image2,requirePlot=True):
    grayImg1 = image1.convert("L")
    grayImg2 = image2.convert("L")
    x=list(grayImg1.getdata())
    y=list(grayImg2.getdata())
    if(requirePlot):
        scatterPlot(x,y)
    return correlation(x,y)

def scatterPlot(x,y):
    plt.scatter(x, y,marker=".", s=4)
    plt.xlabel("X")
    plt.ylabel("")
    plt.title("Scatter Plot")
    plt.show()

def test():
    img1=Image.open("../data/output/scramble/0.png")
    img2=Image.open("../data/output/90.encrypted.png")
    x=toImageCorrelation(img1,img2)
    print(x)

