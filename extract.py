import cv2
import pytesseract
from PIL import Image


def ocr_core(img):

    img=Image.open('test.png')
    text=pytesseract.image_to_string(img)
    print(text)

img=cv2.imread('test.png')

#grey scale conversion
def grey_scale(image):

    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#remove noise from image
def remove_noise(image):

    return cv2.medianBlur(image,5)

#thresholding
def thresholding(image):

    return cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

img=grey_scale(img)
img=remove_noise(img)
img=thresholding(img)

print(ocr_core(img))

