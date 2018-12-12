import cv2 as cv
img = cv.imread("/tmp/test.jpg")
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
cv2.destroyAllWindows()
