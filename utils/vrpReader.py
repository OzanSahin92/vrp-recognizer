import cv2
import pytesseract
import imutils

image = cv2.imread('Germany_BMW.jpg')
image = imutils.resize(image, width=500)

cv2.imshow('resized original image', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('resized gray coloured image', gray)
cv2.waitKey(0)

gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow('resized and smoothed gray coloured image', gray)
cv2.waitKey(0)

edges = cv2.Canny(gray, 170, 200)
cv2.imshow('edges of resized and smoothed gray coloured image', edges)
cv2.waitKey(0)

contours, new = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

copyImage = image.copy()
cv2.drawContours(copyImage, contours, -1, (0, 255, 0), 3)
cv2.imshow('contours in resized and smoothed gray coloured image', copyImage)
cv2.waitKey(0)

contours = sorted(contours, key=cv2.contourArea, reverse=True)[:50]
NumberPlateCount = None

copyImage2 = image.copy()
cv2.drawContours(copyImage2, contours, -1, (0, 255, 0), 3)
cv2.imshow('top 50 contours in resized and smoothed gray coloured image', copyImage2)
cv2.waitKey(0)

counter = 0
name = 1

for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    if len(approx) == 4:
        NumberPlateCount = approx
        x, y, w, h = cv2.boundingRect(contour)
        cropImage = gray[y:y + h, x:x + w]

        cv2.imwrite(str(name) + '.png', cropImage)
        name += 1

        break

cv2.drawContours(image, [NumberPlateCount], -1, (0, 255, 0), 3)
cv2.imshow('final contour in resized and smoothed gray coloured image', image)
cv2.waitKey(0)

croppedVRP = cv2.imread('1.png')
data = pytesseract.image_to_string(croppedVRP, lang='eng', config='--psm 6')
print(data)
