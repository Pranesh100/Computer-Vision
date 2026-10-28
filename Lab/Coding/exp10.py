import cv2

img = cv2.imread("D:/Computer vision/Computer vision Lab/image.jpg")

result = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Rotated 90 Degrees", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
