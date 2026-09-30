import cv2

img = cv2.imread("C:/Users/PRANESH/Downloads/image 1.jpg")
edges = cv2.Canny(img, 100, 200)

cv2.imshow("Original", img)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()