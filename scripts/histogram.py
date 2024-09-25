import sys
from PIL import Image
import matplotlib.pyplot as plt
from entropy import entropy

def main():
    img = Image.open(sys.argv[1])
    grayImg = img.convert("L")
    plt.figure()
    plt.title("Entropy of the image is: "+str(entropy(grayImg)))
    try:    
        plt.suptitle(sys.argv[2]+" image histogram")
    except:
        plt.suptitle("image histogram")
    plt.xlabel("Pixel value")
    plt.ylabel("Frequency")
    histogram=grayImg.histogram()
    pixel_values=list(range(256))
    plt.bar(pixel_values, histogram, width=1, edgecolor='black')
    plt.show()

main()
