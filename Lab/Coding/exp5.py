import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/PRANESH/Downloads/image 1.jpg")

colors = ["b", "g", "r"]

for i, c in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=c)

plt.title("Color Histogram")
plt.xlabel("Color Level")
plt.ylabel("Frequency")
plt.show()

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
