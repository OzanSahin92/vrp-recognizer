import cv2
import pytesseract
import imutils

# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('Special_license_plate_Germany_Berlin.JPG')
image = imutils.resize(image, width=500)

cv2.imshow('resized original image', image)
cv2.waitKey(0)

