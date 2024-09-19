import sys
from PIL import Image
import matplotlib.pyplot as plt

def main():
    img = Image.open(sys.argv[1])
    grayImg = img.convert("L")
    plt.figure()
    try:    
        plt.title(sys.argv[2]+" image histogram")
    except:
        plt.title("image histogram")
    plt.xlabel("Pixel value")
    plt.ylabel("Frequency")
    histogram=grayImg.histogram()
    pixel_values=list(range(256))
    plt.bar(pixel_values, histogram, width=1, edgecolor='black')
    plt.show()

main()
