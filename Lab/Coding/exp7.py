import cv2

cap = cv2.VideoCapture("C:/Users/PRANESH/Downloads/220268_medium.mp4")

speed = 30

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Processing", frame)

    key = cv2.waitKey(speed) & 0xFF

    if key == ord('s'):
        speed = 100
    elif key == ord('f'):
        speed = 1
    elif key == ord('n'):
        speed = 30
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
