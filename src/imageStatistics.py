from PIL import Image
import statistics

def mean(image):
    grayImg = image.convert("L")
    pixel_values = list(grayImg.getdata())
    return statistics.mean(pixel_values)

def median(image):
    grayImg = image.convert("L")
    pixel_values = list(grayImg.getdata())
    return statistics.median(pixel_values) 

def standardDeviation(image):
    grayImg = image.convert("L")
    pixel_values = list(grayImg.getdata())
    return statistics.stdev(pixel_values) 


def test():
    img=Image.open("../data/output/90.encrypted.png")
    print(mean(img))
    print(median(img))
    print(standardDeviation(img))
