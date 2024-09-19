# Image Encryption and Scrambling Project

## Project Structure

```bash
.
├── data/
│ ├── images/ # Input images for processing
│ └── output/ # Output directory for scrambled/encrypted images
│   └── scramble/ # Contains intermediary scrambled images
├── src/ # Source code for image encryption, scrambling, and related algorithms
│ ├── encryption.py # Contains the encryption algorithm
│ ├── scramble.py # C
This project uses:

pillow: Python Imaging Library for image processing.

matplotlib: For plotting histograms of images.


Installation

To install the project in editable mode, use the following command from the root directory:

pip install -e .

This will install the project and allow you to import modules from src in an editable manner.
ontains the scrambling (chaotic map) function
│ └── __init__.py
├── scripts/ # Main scripts for execution
│ ├── main.py # Main script for scrambling and encrypting images
│ ├── histogram.py # Script to generate the histogram of an image
├── docs/ # Documentation for research (optional)
├── setup.py # Setup file for packaging
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files in version control
└── README.md # This file

Requirements

Before running any scripts, make sure you have installed all necessary dependencies. You can do this by installing the requirements using pip:

pip install -e .

Usage

Image Scrambling and Encryption

The main.py script scrambles the image using a chaotic map and performs encryption at the 91st iteration of scrambling.

Example usage:

python scripts/main.py

This will read the image from data/images/, perform scrambling, and output scrambled images and an encrypted image in data/output/.

Image Histogram

To generate a histogram of an image, use the histogram.py script. You need to pass the image file as an argument:

python scripts/histogram.py <image_path> <optional_histogram_title>

Example:

python scripts/histogram.py data/images/4.1.04.tiff "Original Image"

This will generate and display the histogram for the provided image.

Project Overview

Scrambling: The scrambling process uses a Cat Map to rearrange the pixels of the image.

Encryption: The encryption algorithm XORs the scrambled pixel values with chaotic numbers generated using a logistic map.

Histogram Visualization: The histogram script generates the histogram of the pixel values in a grayscale image for visualization purposes.


Directory Details

data/: This directory contains the input and output images. The scrambled and encrypted images are stored here.

src/: Contains the core image processing functions like scrambling (scramble.py) and encryption (encryption.py).

scripts/: Contains the main execution scripts like main.py for image encryption and histogram.py for generating histograms.

docs/: This directory is for documenting research.


