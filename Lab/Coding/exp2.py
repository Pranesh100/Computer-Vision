import cv2
img = cv2.imread("C:/Users/PRANESH/Downloads/image 1.jpg")
blur = cv2.GaussianBlur(img, (5,5), 10)
cv2.imshow("Blur Image", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()