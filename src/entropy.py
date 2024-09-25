import sys
from PIL import Image
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import math

def entropy(image):
    grayImg = image.convert("L")
    pixel_values = list(grayImg.getdata())
    pixel_counts = Counter(pixel_values)
    total_pixels = len(pixel_values)
    probabilities = [count / total_pixels for count in pixel_counts.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy
