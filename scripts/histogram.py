import sys
from PIL import Image
import matplotlib.pyplot as plt
from entropy import entropy

def main():
    img = Image.open(sys.argv[1])
    try:    
        suptitle=(sys.argv[2]+" image histogram")
    except:
        suptitle=("image histogram")
    if(img.mode=="RGB"):
        r,g,b=img.split()
        showHistogram(r,suptitle,1,"red")
        showHistogram(g,suptitle,2,"green")
        showHistogram(b,suptitle,3,"blue")
    else:
        showHistogram(img.convert("L"),suptitle,0,"gray")
    plt.show()

def showHistogram(image,suptitle,figureId,color=""):
    plt.figure(figureId)
    plt.title(("Entropy of the "+color+" image is: "+str(entropy(image))))
    plt.suptitle(suptitle+" "+color)
    plt.xlabel("Pixel intencity")
    plt.ylabel("Frequency of ocarence")
    histogram=image.histogram()
    pixel_values=list(range(256))
    plt.bar(pixel_values, histogram, width=1, edgecolor=color,color=color)
    

main()
