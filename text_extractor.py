from PIL import Image
import PIL.Image
from scan import scanner
import cv2
import numpy as np
import argparse

from pytesseract import image_to_string
import pytesseract 

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned")
args = vars(ap.parse_args())

# Resizing the scanned image according to the given dimensions
warped = scanner(args["image"])

imS = cv2.resize(warped, (1350, 1150))
#cv2.imshow("Output", imS)
cv2.imwrite('Output Image.PNG', imS)
cv2.waitKey(0)

#Extracting text, using the PIL library
#pytesseract.pytesseract.tesseract_cmd = '/usr/share/tesseract-ocr/4.00/tessdata'
#TESSDATA_PREFIX = '/usr/share/tesseract-ocr'
image = PIL.Image.open('Output Image.PNG').convert("RGB")
tessdata_dir_config = "/usr/share/tesseract-ocr/4.00/tessdata"
output = pytesseract.image_to_string(image, lang='eng', config=tessdata_dir_config)

text_file = open("output.txt", "w+")
text_file.write(output)
text_file.close()
